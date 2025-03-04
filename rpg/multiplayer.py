import json
from aqt.qt import *
import aqt.utils
from rpg.game import Game
import aqt
from aqt import mw
import os
import random
import threading
import time
from enum import Enum
from typing import Optional
import aqt
from aqt.qt import *

import pygame
import pytmx
from pygame import Color
import logging
import PygameUIKit
from scripts.utils import get_data
from rpg.ParticleSystem import EffectManager, Particle
from rpg.config import Colors
from rpg.engine import Player, Engine, Mob, Mode
from rpg.popups import SaveWindow, ActionWindow
from rpg.network import Network
from rpg.game import Game
from pathlib import Path
from aqt import *
from scripts.utils import center_widget
import pickle
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

cwd = os.path.dirname(__file__)
parent = os.path.dirname(cwd)
data_path = os.path.join(parent, 'anki_data.json') 
info = pygame.display.Info()
size = info.current_w,info.current_h
BOUNDING_RECT = pygame.Rect(-600+info.current_w/3, -700, 1000, 200)

class PlayerType(Enum):
    Human = 1
    Bot = 2


class MultiPlayerRpg:
    def __init__(self, win:pygame.Surface, ankimons:dict, trainer):
        self.win = win
        self.clock = pygame.time.Clock()
        self.running = False
        self.map = Pytmx(self.win)
        self.highlighted_tile = None
        self.ankimons = ankimons
        self.ankiwin = None
        self.trainer = trainer
        self.move = 0
        
        self.players = {
            Player.Player1: PlayerType.Human,
            Player.Player2: PlayerType.Bot
        }

        self.completed_cards = 0
        self.selected_tile = None
        self.last_move = time.time()
        self.accessible_tiles = []
        self.attackable_tiles = []
        self.trainer_xp = get_data().get('trainer_xp')

        self.font = pygame.font.SysFont('comicsans', 36)
        self.group = PygameUIKit.Group()
        common = {
            "ui_group": self.group,
            "border_radius": 10,
            "text_align": "center",
            "fixed_width": 300,
        }
        
        self.selected_mon: Optional[Mob] = None
        self.counter = 0
        self.learned_cards = 0
        self.network = Network()
        self.game : Game= None
        self.p = None
        while self.p == None:
            try:
                self.p = int(self.network.getP())
            except Exception as e:
                print(e)
            self.draw()
            text = self.font.render("Server's are currently unavailable", True, (255,255,255))
            self.win.blit(text, (self.win.get_width()/2-text.get_width()/2, 15))
        
            print(f"you are player: {self.p}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    mw.win = None
                    return
            pygame.display.flip()
        self.idle()
        aqt.utils.showInfo('You have 10 minutes to learn the most cards whoever learns the most will have the first move')
        self.learn() 
        self.engine = Engine(self.map.free_places, ankimons, self.win, self.map, trainers=trainer)
        self.learned_card_checker()


    def learned_card_checker(self):
        with open(data_path, "r") as f:
            data = json.load(f)
        if 'moves' not in data:
            self.learned_cards = data['nb_cards_learned_today']
            data['moves'] = self.learned_cards
            json.dump(data, open(data_path, 'w'))
        else:
            self.learned_cards = data['moves']

    def idle(self):
        while 1:
            self.clock.tick(60)
            self.draw()
            pygame.display.flip()
            self.game = self.network.send({'ankimons': self.ankimons, 'trainer':self.trainer})
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    mw.win = None
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
            if self.game.data[not self.p]:
                return 
    
    def learn(self):
        start_time = self.game.learning_start
        while True:
            self.clock.tick(60)
            self.draw()
            text = self.font.render(f"Time left: {(time.time() - start_time)//60}:{(time.time() - start_time)%60}")
            self.win.blit(text, (self.win.get_width()/2 - text.get_width()/2, 15))
            pygame.display.flip()
            self.game = self.network.send({'cards_learned': get_data().get('trainer_xp') - self.trainer_xp})
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass

    def run(self):
        self.running = True
        frame = 0 
        self.ankiwin = ActionWindow('move', 10)
        while self.running:
            self.clock.tick(60)
            frame = (frame+1) % 60
            # print(f"\rFPS: {self.clock.get_fps()}", end="")
            if frame%10 == 0:
                self.learned_card_checker()
            self.events()
            self.update()
            self.draw()
            pygame.display.flip()
            # print(self.clock.get_fps())
    
        
    def events(self):
        events = pygame.event.get()
        for event in events:
            self.group.handle_event(event)
            if event.type == pygame.QUIT:
                self.running = False

            if self.players.get(self.engine.turn) == PlayerType.Human:
                if event.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    self.highlighted_tile = x, y
                if self.engine.mode == Mode.Idle:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        j, i = self.map.iso_to_ortho(*self.highlighted_tile)
                        if not (j, i) in self.map.free_places:
                            return
                        arena_i, arena_j = i, j
                        if self.engine.contains_mob(arena_i, arena_j):
                            mob = self.engine.get_mob(arena_i, arena_j)
                            if mob.owner == self.engine.turn:
                                self.selected_mon = mob
                                self.selected_tile = (arena_i, arena_j)
                                self.change_mode(Mode.active)
                                self.accessible_tiles = self.engine.get_moves((arena_i, arena_j))
                                self.attackable_tiles = self.engine.get_attackable_cases((arena_i, arena_j))


                elif self.engine.mode == Mode.active and self.learned_cards >= 1:
                    self.handle_event(event)

        move = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]:
            self.map.x_start += move[0]
            self.map.y_start += move[1]
            # clamp
            self.map.x_start = min(max(self.map.x_start, BOUNDING_RECT.left), BOUNDING_RECT.right)
            self.map.y_start = min(max(self.map.y_start, BOUNDING_RECT.top), BOUNDING_RECT.bottom)

    def handle_event(self, event):
        if not self.selected_mon:
            return
    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            j, i = self.map.iso_to_ortho(*self.highlighted_tile)
            if (j, i) not in self.map.free_places:
                return
            if self.engine.perform_move((self.selected_mon.i, self.selected_mon.j), (i, j)):
                self.learned_cards -= 1
                data = json.load(open(data_path, 'r'))
                data['moves'] = self.learned_cards
                json.dump(data, open(data_path, 'w'))
                self.last_move = time.time()

            elif self.engine.perform_attack((self.selected_mon.i, self.selected_mon.j), (i, j)):
                
                self.learned_cards -= 1
                data = json.load(open(data_path, 'r'))
                data['moves'] = self.learned_cards
                json.dump(data, open(data_path, 'w'))
                self.last_move = time.time()
            self.selected_mon = None
            self.selected_tile = None
            self.change_mode(Mode.Idle)
            

    def update(self):
        pass

    def draw(self):
        self.win.fill(Color("black"))
        self.map.draw(self.win)
        self.draw_arena()
        if self.highlighted_tile:
            j, i = self.map.iso_to_ortho(*self.highlighted_tile)
            # draw only if in arena
            if (j, i) in self.map.free_places:
                pygame.draw.polygon(self.win, Color("red"),
                                    [
                                        self.map.ortho_to_iso(j, i),
                                        self.map.ortho_to_iso(j + 1, i),
                                        self.map.ortho_to_iso(j + 1, i + 1),
                                        self.map.ortho_to_iso(j, i + 1)
                                    ], 2)
        if self.selected_tile:
            i, j = self.selected_tile[0], self.selected_tile[1]

            pygame.draw.polygon(self.win, Color("blue"),
                                [
                                    self.map.ortho_to_iso(j, i),
                                    self.map.ortho_to_iso(j + 1, i),
                                    self.map.ortho_to_iso(j + 1, i + 1),
                                    self.map.ortho_to_iso(j, i + 1)
                                ], 2)

        # show whose turn it is
        text = ""
        try:
            text = "Your turn" if self.engine.turn == Player.Player1 else "Opponent's turn"
        except AttributeError:
            if self.p != None:
                text = "searching for oppenents"
        
        text = self.font.render(text, True, Color("white"))
        self.win.blit(text, (self.win.get_width()/2 - text.get_width()/2, 10))


    def draw_arena(self):
        try:
            for mob in self.engine.get_all_mobs():
                mob.draw(self.map)
        except AttributeError:
            pass
        
        if self.selected_mon and self.engine.mode == Mode.active:
            for i, j in self.attackable_tiles:
                x, y = self.map.ortho_to_iso(j, i)
                x += 0
                y += 20
                pygame.draw.circle(self.win, Color("pink"), (x, y), 5)
        if self.selected_mon and self.engine.mode == Mode.active:
            for i, j in self.accessible_tiles:
                if self.engine.contains_mob(i, j):
                    continue
                x, y = self.map.ortho_to_iso(j, i)
                x += 0
                y += 20
                pygame.draw.circle(self.win, Color("red"), (x, y), 5)


    def change_mode(self, mode: Mode):
        self.engine.mode = mode


class Pytmx:
    def __init__(self, win):
        self.win = win
        self.data_tmx = pytmx.load_pygame(os.path.join(cwd, "assets", "map", "map.tmx"))
        self.zoom = 3
        self.x_start, self.y_start = 500, -500

        self.zoomed_tile_width = self.data_tmx.tilewidth * self.zoom
        self.zoomed_tile_height = self.data_tmx.tileheight * self.zoom

        self.free_places: list[tuple[int, int]] = []

        for k, v in enumerate(self.data_tmx.images):
            if not v:
                continue
            self.data_tmx.images[k] = pygame.transform.scale(v, (
                int(v.get_width() * self.zoom), int(v.get_height() * self.zoom)))

        self.load_free_places()

    def load_free_places(self):
        for layer in self.data_tmx.visible_layers:
            for j, i, gid in layer:
                if gid == 2:
                    self.free_places.append((j + 1, i))  # Fix to make it look better
        

    def ortho_to_iso(self, j: int, i: int) -> tuple[float, float]:
        return ((j - i) * self.zoomed_tile_width / 2 + self.x_start,
                (j + i) * self.zoomed_tile_height / 2 + self.y_start)

    def iso_to_ortho(self, x, y) -> tuple[int, int]:
        j = int((x - self.x_start) / self.zoomed_tile_width + (y - self.y_start) / self.zoomed_tile_height)
        i = int((y - self.y_start) / self.zoomed_tile_height - (x - self.x_start) / self.zoomed_tile_width)
        return j, i

    def draw(self, win):
        for layer in self.data_tmx.visible_layers:
            for j, i, gid in layer:
                tile = self.data_tmx.get_tile_image_by_gid(gid)
                if tile:
                    win.blit(tile, self.ortho_to_iso(j, i))
