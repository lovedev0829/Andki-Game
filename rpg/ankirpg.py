import json
import os
import random
import time
from enum import Enum
from typing import Optional

import pygame
import pytmx
from pygame import Color
import logging
import PygameUIKit
from rpg.ParticleSystem import EffectManager, Particle
from rpg.config import Colors
from rpg.engine import Player, Engine, Mob, Mode, Trainer, fps_counter
from rpg.popups import SaveWindow, ActionWindow, trainer_popup, Win_popup, WildAnkimon, learned_card_checker, center_win
from rpg.utils import handle_item
from rpg.tmx import Pytmx
from pathlib import Path
from aqt import mw
from scripts.utils import center_widget, get_data, change_data
from aqt.qt import *
import pickle
from scripts.constants import *
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

class Actions(Enum):
    MOVE = 'move'
    ATTACK = 'attack'
    DEFEND = 'defend'


class Costs(Enum):
    ATTACK = 10
    DEFEND = 10
    MOVE = 5
    CHALLENGE = 10
    WILD = 50



class AnkiRPG:
    def __init__(self, win:pygame.Surface, ankimons:dict, trainers:list[Trainer], load_save:bool=False):
        self.win = win
        self.clock = pygame.time.Clock()
        self.running = False
        self.map = Pytmx(self.win)
        self.wild_ankimon_chance = 0.1
        self.highlighted_tile = None
        self.ankimons = ankimons
        self.ankiwin = None
        self.ratio = 0
        self.load_save = load_save
        self.trainers = trainers
        self.engine = Engine(self.map.free_places, ankimons, self.win, self.map, self.trainers)
                
        self.MULTIPLIER = get_data().get('Difficulty',1)
        # self.MULTIPLIER = 0.02
        self.players = {
            Player.Player1: PlayerType.Human,
            Player.Player2: PlayerType.Bot
        }

        self.completed_cards = 0
        self.selected_tile = None
        self.last_move = time.time()
        self.accessible_tiles = []
        self.attackable_tiles = []

        self.trainer_xp = get_data().get('trainer_xp',0)
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
        self.learned_card_checker()
        self.game_over = False
        self.savewin = None
        self.completed_cards = self.learned_cards
        handle_item(self, self.engine)
        if load_save:
            self.load()


    def learned_card_checker(self):
        with open(data_path, "r") as f:
            data = json.load(f)
        if 'moves' not in data:
            self.learned_cards = data['nb_cards_learned_today']
            data['moves'] = self.learned_cards
            json.dump(data, open(data_path, 'w'))
        else:
            self.learned_cards = data['moves']

    
    def run(self):
        self.running = True
        frame = 0 
        if not self.ankiwin:
            self.ankiwin = trainer_popup(int(Costs.CHALLENGE.value*self.MULTIPLIER), self.trainers[1].name)
            center_win(self.ankiwin)
            self.ankiwin.cards = learned_card_checker(data_path)

        while self.running:
            self.clock.tick(60)
            
            frame = (frame+1) % 60
            # print(f"\rFPS: {self.clock.get_fps()}", end="")
            if frame%10 == 0:
                self.learned_card_checker()
                self.update_anki()
            try:
                self.events()
            except pygame.error as e:
                print(e)
                break
            if not self.ankiwin:
                self.bot_event()
            
            self.update()
            
            self.draw()
            
            # print(self.clock.get_fps())
        mw.win = None
        if not self.savewin and self.engine.player1_mobs and self.engine.player2_mobs:
            self.savewin = SaveWindow(self.save, self)

    def update_anki(self):
        self.MULTIPLIER = get_data().get('Difficulty',1)
        if not mw.col.sched.get_queued_cards().cards:
            self.savewin = SaveWindow(self.save, self)
            self.label = QLabel("""The gamified learning is over 
    do you want to save your progress?""")
            self.game_over = True
            self.running = False
        mw.win = self.ankiwin
        if self.ankiwin:
            if not self.game_over:
                self.ankiwin.completed_cards = round((self.learned_cards - self.completed_cards) *10)
                if isinstance(self.ankiwin, WildAnkimon):
                    self.ankiwin.text_label.setText(f"""   A wild ankimon has approached you, learn {self.ankiwin.required_cards} cards to capture it    
        {self.ankiwin.completed_cards}/{self.ankiwin.required_cards}""")
                    self.ankiwin.update()

                if not hasattr(self.ankiwin, 'action'):
                    self.ankiwin.completed_cards = int((self.learned_cards-self.ankiwin.cards)*10)
                    if self.load_save:
                        self.ankiwin.text_label.setText(f"""There you are again, want to keep playing? 
        Then learn {self.ankiwin.cost} cards for me.

                            {self.ankiwin.completed_cards}/{self.ankiwin.cost}""")
                    else:
                        self.ankiwin.text_label.setText(f"""So you want to take on the next challenge?
        I'll show you that I'm the best 
        AnkiMon trainer here, not you!
        learn {self.ankiwin.cost} cards to accept the challenge
                                    {self.ankiwin.completed_cards}/{self.ankiwin.cost}
                                        """)
                    self.ankiwin.text_label.adjustSize()    
                    if self.ankiwin.completed_cards >= self.ankiwin.cost:
                        self.ankiwin = None
                        
                    return
                else:
                    if self.ankiwin.action == Actions.DEFEND:
                        self.ankiwin.label.setText(f"""Damn, someone is attacking you! Defend yourself by learning {self.ankiwin.required_cards} cards!!!
                                
                                        {self.ankiwin.completed_cards}/{self.ankiwin.required_cards}                                       """)
                        if not hasattr(self.ankiwin, 'skipbutton'):
                            self.ankiwin.skipbutton = QPushButton(self.ankiwin)
                            self.ankiwin.skipbutton.setText('Skip the Cards and take full damage')
                            self.ankiwin.skipbutton.adjustSize()
                            self.ankiwin.skipbutton.move(int(self.ankiwin.width()/2),int(250) - int(self.ankiwin.height()/2))
                            self.ankiwin.skipbutton.clicked.connect(lambda : self.engine.perform_attack(self.ankiwin.coords[0], self.ankiwin.coords[1]) and self.ankiwin.close())
                            self.ankiwin.skipbutton.show()
                            self.ankiwin.skipbutton.setChecked(False)
                    elif self.ankiwin.action:
                        self.ankiwin.label.setText(f"""You want to {self.ankiwin.action.value}, give me {self.ankiwin.required_cards} cards!!!
                        
                                                                        
                                        {self.ankiwin.completed_cards}/{self.ankiwin.required_cards}                                       """)
                    if self.ankiwin.completed_cards >= self.ankiwin.required_cards:
                        if not self.ankiwin.action:
                            self.ankiwin.close()
                        elif self.ankiwin.action == Actions.MOVE:
                            self.engine.perform_move(*self.ankiwin.coords)
                            coords = self.ankiwin.coords
                            self.ankiwin = None
                            self.completed_cards = self.learned_cards
                            self.last_move = time.time()
                            if random.random() <= self.wild_ankimon_chance:
                                self.ankiwin = WildAnkimon(int(Costs.WILD.value*self.MULTIPLIER), coords, self)
                                # raise NotImplementedError('didnt implement wild ankimons')
                        elif self.ankiwin.action == Actions.ATTACK:
                            self.engine.perform_attack(*self.ankiwin.coords)
                            self.ankiwin = None
                            self.completed_cards = self.learned_cards
                            self.last_move = time.time()
                            if  not self.engine.player2_mobs:
                                self.ankiwin = Win_popup(self, won=True)
                                try:
                                    os.remove(SAVE_PATH)
                                except FileNotFoundError:
                                    pass
                                self.game_over = True                            
                        elif self.ankiwin.action == Actions.DEFEND:
                            self.engine.get_mob(*self.ankiwin.coords[1]).defense *= 1.4
                            self.engine.perform_attack(*self.ankiwin.coords)
                            if (mob :=self.engine.get_mob(*self.ankiwin.coords[1])):
                                mob.defense /= 1.4
                                mob.blocked = True
                            self.ankiwin = None
                            self.completed_cards = self.learned_cards            
                            if  not self.engine.player1_mobs:
                                self.ankiwin = Win_popup(self, False)
                                try:
                                    os.remove(SAVE_PATH)
                                except FileNotFoundError as e:
                                    print(e)
                                self.game_over = True                                        
                        
        else:
            self.completed_cards = self.learned_cards
            if  not self.engine.player2_mobs:
                self.ankiwin = Win_popup(self, won=True)
                try:
                    os.remove(SAVE_PATH)
                except FileNotFoundError as e:
                    print(e)
                self.game_over = True                            
                 
            if  not self.engine.player1_mobs:
                self.ankiwin = Win_popup(self, False)
                try:
                    os.remove(SAVE_PATH)
                except FileNotFoundError as e:
                    print(e)
                self.game_over = True                                        
    
    def save(self):
        for mob in self.engine.player1_mobs+self.engine.player2_mobs:
            mob.img = None
            mob.screen = None
            mob.font = None
            mob.smallfont = None
            mob.manager = None
            mob.engine = None
            mob.attacked_ankimon = None
        self.learned_card_checker()
        data = {
            "turn": self.engine.turn,
            'player1_mobs' : self.engine.player1_mobs,
            'player2_mobs' : self.engine.player2_mobs,
            'completed_cards' : self.completed_cards,
            'ankiwin' : [self.ankiwin.action, self.ankiwin.required_cards, self.ankiwin.coords, round((self.learned_cards - self.completed_cards) *10)] if self.ankiwin and hasattr(self.ankiwin,'action') else None,
            'trainer_name' : self.trainers[1].name,
        }

        
        pickle.dump(data, open(SAVE_PATH, 'wb'))
    @staticmethod
    def check():
        data = pickle.load(open(SAVE_PATH, 'rb'))
        data['turn']
        data['player1_mobs']
        data['player2_mobs']
        data['completed_cards']
        data['trainer_name']
    def load(self):
        try:
            AnkiRPG.check()
        except Exception as e:
            print(e)
            return 
        data = pickle.load(open(SAVE_PATH, 'rb'))
        self.engine.turn = data['turn']
        self.engine.player1_mobs = data['player1_mobs']
        self.engine.player2_mobs = data['player2_mobs']
        self.completed_cards = data['completed_cards']
        self.trainers[1].name = data['trainer_name']
        if data['ankiwin']:
            self.ankiwin = ActionWindow(data['ankiwin'][0], data['ankiwin'][1], data['ankiwin'][2], self)
            self.ankiwin.completed_cards = data['ankiwin'][3]

        for mob in self.engine.player1_mobs + self.engine.player2_mobs:
            mob.img = mob.load_image()
            mob.screen = self.win
            mob.manager = EffectManager(self.win, self.map)
            mob.font = pygame.font.SysFont("Comicsans", 26)
            mob.smallfont = pygame.font.SysFont("Comicsans", 16)
            mob.engine = self.engine

    def bot_event(self):    
        if self.players.get(self.engine.turn) != PlayerType.Bot:
            return
        if time.time() - self.last_move < 1.3:
            return
        for mob in self.engine.player2_mobs:
            i, j = mob.i, mob.j
            accessible = self.engine.get_attackable_cases((i, j))
            for move in random.choice([accessible]):
                if self.engine.attack_condition((i, j), move):
                    self.ankiwin = ActionWindow(Actions.DEFEND, int(Costs.DEFEND.value*self.MULTIPLIER), ((i, j), move), self)
                    return
        if not self.engine.player2_mobs:
            return
        if not mob:
            return
        mob = random.choice(self.engine.player2_mobs)
        i, j = mob.i, mob.j
        accessible = self.engine.get_moves((i, j))
        move = random.choice(accessible)
        self.engine.perform_move((i, j), move)

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
            if not self.ankiwin:
                j, i = self.map.iso_to_ortho(*self.highlighted_tile)
                if (j, i) not in self.map.free_places:
                    return
                coords = (self.selected_mon.i, self.selected_mon.j), (i, j)
                if self.engine.move_condition(*coords):
                    self.ankiwin = ActionWindow(Actions.MOVE, int(Costs.MOVE.value*self.MULTIPLIER), coords, self)
                    

                elif self.engine.attack_condition(*coords):
                    self.ankiwin = ActionWindow(Actions.ATTACK, int(Costs.ATTACK.value*self.MULTIPLIER), coords, self)
                self.change_mode(Mode.Idle)
                self.selected_mon = None
                self.selected_tile = None
                
            self.learned_card_checker()
            
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
        text = "Your turn" if self.engine.turn == Player.Player1 else "Opponent's turn"
        text = self.font.render(text, True, Color("white"))
        self.win.blit(text, (self.win.get_width()/2 - text.get_width()/2, 10))
        fps_counter(self.clock, self.font, self.win)
        pygame.display.flip()

    def draw_arena(self):
        for i,mob in enumerate(self.engine.get_all_mobs()):
            
            mob.draw(self.map)
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

