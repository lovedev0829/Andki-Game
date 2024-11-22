from enum import Enum
from typing import Optional
import images
from rpg.ParticleSystem import EffectManager, Particle, Colors
from rpg.utils import *
from scripts.constants import streak_data_path, anki_data_path, streak_ankimon_path
import pygame
from pygame import Color
import logging
import time
import json
import random
# from rpg.ankirpg import Pytmx
logging.basicConfig()

# logging.root.setLevel(logging.NOTSET)

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger('game')

MAX_MOVE_DISTANCE = 3
import math
pygame.init()

class Trainer:
    def __init__(self, name, attack, defense,movement=0):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.movement = movement
 
def fps_counter(clock, font:pygame.font.Font, screen:pygame.Surface):
    fps = str(int(clock.get_fps()))
    
    fps_t = font.render(fps , 1, pygame.Color("green"))
    
    screen.blit(fps_t,(0,0))

class Mob:
    def __init__(self, i, j, name, element, owner: "Player", screen, map_t, trainer:Trainer, engine, health=100):
        self.i = i
        self.j = j
        print(trainer)
        self.old_pos = [i, j]
        self.engine = engine
        self.name = name
        self.element:str = element
        self.trainer = trainer
        self.img = self.load_image()
        self.health = health
        self.maxhealth = self.health
        self.defense = 1
        self.dmg = 10
        self.last_attack = time.time() -2
        self.last_damaged = 0
        self.screen = screen
        self.blocked = False
        self.last_attacked = time.time() -2
        self.time = time.time()-2
        self.manager = EffectManager(self.screen, map_t)
        self.owner = owner
        self.defense *= trainer.defense
        self.dmg *= trainer.attack
        self.attacking_ankimon = None
        self.font = pygame.font.SysFont("Comicsans", 26)
        self.smallfont = pygame.font.SysFont("Comicsans", 16)
        self.attacked_ankimon = None
        
    
    def load_image(self):
        return images.load_mob_img(self.name)

    def move(self, i, j):
        self.i = i
        self.j = j

    def attack(self, mob: "Mob"):
        multiplier = 1
        if self.element.lower() == 'fire' and mob.element.lower() == 'ice':
            multiplier = 1.2
        elif self.element.lower() == 'ice' and mob.element.lower() == 'fire':
            0.8
        elif self.element.lower() == 'water' and mob.element.lower() == 'fire':
            multiplier = 1.2
        elif self.element.lower() == 'fire' and mob.element.lower() == 'water':
            multiplier = 0.8
        elif self.element.lower() == 'ice' and mob.element.lower() == 'water':
            multiplier = 1.2
        elif self.element.lower() == 'water' and mob.element.lower() == 'ice':
            multiplier = 0.8
        print(f"element:{self.element}, defender:{mob.element}, multiplier:{multiplier}")
        self.last_attack = time.time()
        self.attacked_ankimon = mob
        mob.lost_health(self.dmg*multiplier, self)
        self.engine.vfx[self.element.upper()][0].reset()
        self.engine.vfx[self.element.upper()][1].reset()
        self.engine.vfx[self.element.upper()][2].reset()    
    
    def lost_health(self, dmg, ankimon):
        dmg/=self.defense
        if self.health > dmg:
            self.last_damaged = dmg
        else:
            self.last_damaged = self.health
        self.health = max(0, self.health - dmg)
        self.last_attacked = time.time()
        print(dmg)
        if self.health == 0:
            self.owner = None
        self.attacking_ankimon = ankimon
        self.engine.vfx[self.element.upper()][0].reset()
        self.engine.vfx[self.element.upper()][1].reset()
        self.engine.vfx[self.element.upper()][2].reset()
        print(self.engine.vfx[self.element.upper()][1])
        print(self.engine.vfx[self.element.upper()][1].frame)
        print(self.engine.vfx[self.element.upper()][1].dur)
        print(self.engine.vfx[self.element.upper()][1].done)

    def draw(self, map_t):
        x, y = map_t.ortho_to_iso(self.j, self.i)
        old_pos = map_t.ortho_to_iso(self.old_pos[1], self.old_pos[0])
        self.manager.update()
        interval = 0.5
        if time.time() - self.time > interval:
            if self.element.lower() == 'fire':
                self.manager.add_particle((x,y), Colors.FIRE.value)
            if self.element.lower() == 'water':
                self.manager.add_particle((x,y), Colors.WATER.value)  
            if self.element.lower() == 'ice':
                self.manager.add_particle((x,y), Colors.ICE.value)
        if time.time() -  self.last_attacked < 1:
            if round((time.time() - self.last_attacked)%1*10) %2 == 0:
                self.screen.blit(self.img, (x - 32, y - 24))
            text = self.font.render(f"-{int(self.last_damaged)}", 1, (255, 0, 0))
            text.set_alpha(255*(1-(time.time() -  self.last_attacked)))
            self.screen.blit(text, (x ,y- (time.time() -  self.last_attacked)*100))
            if self.blocked:
                text = self.smallfont.render(f"blocked", 1, (255, 0, 0))
                text.set_alpha(255*(1-(time.time() -  self.last_attacked)))
                self.screen.blit(text, (x- 30,y - 30- (time.time() -  self.last_attacked)*100))            
        else:
            self.blocked = False
            self.old_pos[0] += (self.i - self.old_pos[0])/4
            self.old_pos[1] += (self.j - self.old_pos[1])/4
            self.screen.blit(self.img, ((x - 32 + old_pos[0]-32)/2, (y - 24 + old_pos[1]-24)/2))
        if time.time() -  self.last_attack < 0.5 and self.attacked_ankimon:
            animation = self.engine.vfx[self.element.upper()][1]
            # anim is for the animation for starting the attack
            anim = self.engine.vfx[self.element.upper()][0]
            if self.element.lower() == 'ice':
                offset = throw((x,y), map_t.ortho_to_iso(self.attacked_ankimon.j, self.attacked_ankimon.i), (time.time() - self.last_attack)*2,-120)
                self.screen.blit(animation.img(), (x+offset[0]-190,y+offset[1]-175))
                self.screen.blit(anim.img(), (x-170,y-265))
                
            elif self.element.lower() == 'fire':
                pos = map_t.ortho_to_iso(self.attacked_ankimon.j, self.attacked_ankimon.i)
                angle = math.degrees(math.atan2(pos[1]-y, x-pos[0])+math.pi)-90
                offset = throw((x,y), pos, (time.time() - self.last_attack)*2)
                self.screen.blit(pygame.transform.rotate(animation.img(), angle), (x+offset[0]-animation.img().get_rect().centerx,y+offset[1]-animation.img().get_rect().centery))
                # self.screen.blit(anim.img(), (x-30,y-100))
            else:
                pos = map_t.ortho_to_iso(self.attacked_ankimon.j, self.attacked_ankimon.i)
                angle = math.degrees(math.atan2(pos[1]-y, x-pos[0])+math.pi)-90
                offset = throw((x,y), pos, (time.time() - self.last_attack)*2)
                self.screen.blit(pygame.transform.rotate(animation.img(), angle), (x+offset[0]-animation.img().get_rect().centerx,y+offset[1]-animation.img().get_rect().centery))
                # self.screen.blit(anim.img(), (x,y))
            
            anim.update()
            animation.update()
            print(anim.frame)
        if time.time() - self.last_attacked > 0.5 and time.time() - self.last_attacked < 1 and self.attacking_ankimon:
            animation = self.engine.vfx[self.attacking_ankimon.element.upper()][2]
            animation.dur = 3
            if self.attacking_ankimon.element.lower() == 'fire':
                self.screen.blit(animation.img(), (x-45, y-70))
            elif self.attacking_ankimon.element.lower() == 'water':
                self.screen.blit(animation.img(), (x-65, y-90))
            else:self.screen.blit(animation.img(), (x-165, y-190))
            animation.update()
        #### Lines below used for testing animations
        # for i, image in enumerate(self.engine.vfx['FIRE'][2].images):
        #     self.screen.blit(image, (i*50,0))
        # if self.attacked_ankimon:
        #     points = []
        #     for i in [0.1* i for i in range(11)]:
        #         p=throw((x,y), map_t.ortho_to_iso(self.attacked_ankimon.j, self.attacked_ankimon.i), i,1)
        #         points.append([p[0]+x, p[1]+y])
        #     for i, point in enumerate(points):
        #         self.screen.blit(self.engine.vfx['FIRE'][1].images[i%len(self.engine.vfx['FIRE'][1].images)],point)
        #     pygame.draw.lines(self.screen, (0,0,0), False, points)
        # Health bar ally
        if self.owner == Player.Player1:
            pygame.draw.rect(self.screen, Color("red"), (x - 16, y - 16, 32, 4))
            pygame.draw.rect(self.screen, Color("green"), (x - 16, y - 16, 32 * self.health / 100, 4))
        else:
            pygame.draw.rect(self.screen, Color("black"), (x - 16, y - 16, 32, 4))
            pygame.draw.rect(self.screen, Color("red"), (x - 16, y - 16, 32 * self.health / 100, 4))

class Player(Enum):
    Player1 = 1
    Player2 = 2


class Mode(Enum):
    Idle = 0
    active = 1



class Engine:
    def __init__(self, free_places, ankimons: dict, screen, map_t, trainers:list[Trainer], enemy_levels: list[int] = None):
        self.turn: Player = Player.Player1
        self.free_places: list[tuple[int, int]] = free_places  # List of (i, j) tuples
        self.player1_mobs: list[Mob] = []
        self.player2_mobs: list[Mob] = []
        self.vfx = load_dir(os.path.join(os.path.dirname(__file__), 'assets', 'VFX'))
        self.vfx['FIRE'][0].dur += 1
        for element in self.vfx.keys():
            if element == 'ICE':continue
            for animation in self.vfx[element]:
                for i, image in enumerate(animation.images):
                    biggest_rect = None
                    rects = pygame.mask.from_surface(image).get_bounding_rects()
                    if rects:
                        biggest_rect=get_enclosing_rect(pygame.mask.from_surface(image).get_bounding_rects())
                    if biggest_rect:
                        s = pygame.Surface(biggest_rect.size)
                        s.set_colorkey((0,0,0))
                        s.blit(image, (0,0), biggest_rect)
                        animation.images[i] = s
        names = list(ankimons.keys()) 
        if len(ankimons.keys()) == 3:
            names.extend(ankimons.keys())
        if ankimons:
            self.add_mob(Mob(24, 21, names[0], ankimons[names[0]], Player.Player1, screen, map_t, trainers[0], self))
            self.add_mob(Mob(25, 21, names[1], ankimons[names[1]], Player.Player1, screen, map_t, trainers[0], self))
            self.add_mob(Mob(26, 21, names[2], ankimons[names[2]], Player.Player1, screen, map_t, trainers[0], self))
            self.add_mob(Mob(17, 24, names[0], ankimons[names[3]], Player.Player2, screen, map_t, trainers[1], self))
            self.add_mob(Mob(18, 24, names[1], ankimons[names[4]], Player.Player2, screen, map_t, trainers[1], self))
            self.add_mob(Mob(21, 24, names[2], ankimons[names[5]], Player.Player2, screen, map_t, trainers[1], self))
        

        ankimon_data = json.load(open(streak_ankimon_path, 'r'))
        levels = [ankimon_data[anki].get('level') for anki in ankimon_data.keys()]
        for i, mob in enumerate(self.player1_mobs):
            mob.defense += 0.2*levels[i]
            mob.dmg += 0.2*levels[i]
        if not enemy_levels:
            enemy_levels = [max(1, level + random.randint(-3,3)) for level in levels]
            for i, mob in enumerate(self.player2_mobs):
                mob.defense += 0.2*enemy_levels[i]
                mob.dmg += 0.2*enemy_levels[i]            
        self.mode: Mode = Mode.Idle
        
        
    def add_mob(self, mob: Mob):
        player = mob.owner
        if player == Player.Player1:
            self.player1_mobs.append(mob)
        else:
            self.player2_mobs.append(mob)

    def contains_mob(self, i: int, j: int) -> bool:
        return (i, j) in [(mob.i, mob.j) for mob in self.player1_mobs + self.player2_mobs]

    def is_place_empty(self, i: int, j: int) -> bool:
        """Returns True if the place is not a terrain and no mob is on it"""
        return (j, i) in self.free_places

    def get_mob(self, i: int, j: int) -> Optional[Mob]:
        for mob in self.player1_mobs + self.player2_mobs:
            if mob.i == i and mob.j == j:
                return mob
        return None

    def perform_move(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        logger.debug(f"Trying to move from {start} to {end}")
        mob = self.get_mob(*start)
        if self.move_condition(start, end):
            mob.move(*end)
            neighbors = filter(lambda x: self.contains_mob(*x) and self.get_mob(*x).owner != self.turn, self.get_neighbors(*end))
            for neighbor in neighbors:
                1
                # self.get_mob(*neighbor).attack(mob)
            self.switch_turn()
            return True

    def move_condition(self, start, end):
        if start == end: return False
        if not self.is_place_empty(*end):
            logger.debug("End place is not empty")
            return False
        if (end[0], end[1]) not in self.get_moves((start[0], start[1])):
            logger.debug("End place is not accessible")
            return False
        return True
        
    def perform_attack(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        logger.debug(f"Trying to attack from {start} to {end}")
        attacker = self.get_mob(*start)
        defender = self.get_mob(*end)
        
        if self.attack_condition(start, end):
            
            attacker.attack(defender)
            if defender.health <= 0:
                if defender in self.player1_mobs:
                    self.player1_mobs.remove(defender)
                else:
                    self.player2_mobs.remove(defender)
            self.switch_turn()
            return True

    def attack_condition(self, start, end):
        attacker = self.get_mob(*start)
        defender = self.get_mob(*end)
        
        if start == end: 
            logger.debug(f"The end square is the same as the beggining square")
            return False
        
        if not defender: 
            logger.debug("No defender found")
            return False
        if attacker.owner == defender.owner:
            logger.debug("Can't attack an ally")
            return False
        if (end[0], end[1]) not in self.get_attackable_cases((start[0], start[1])):
            logger.debug("End place is not accessible")
            return False        
        return True
    def switch_turn(self):
        self.turn = Player.Player1 if self.turn == Player.Player2 else Player.Player2

    def get_all_mobs(self):
        return self.player1_mobs + self.player2_mobs

    def get_accessible_cases(self, start: tuple[int, int], element=None) -> list[tuple[int, int]]:
        if not element:
            element = self.get_mob(*start).element.lower()
        element = element.lower()
        if element == 'fire':
            max_dist = 2
        else:
            max_dist = 3
        mob = self.get_mob(*start)
        max_dist += mob.trainer.movement
        moves = set()
        pos = start
        if element == 'water':
            for i in range(-max_dist, max_dist+1):
                if self.is_place_empty(i+pos[0], pos[1]):
                    moves.add((i+pos[0],pos[1]))
                if self.is_place_empty(pos[0], i+pos[1]):
                    moves.add((pos[0], i+pos[1]))                    
            return list(moves)
        if element == 'ice':
            for i in range(-max_dist, max_dist+1):
                pos1 = i+pos[0], i+pos[1]
                if self.is_place_empty(*pos1):
                    moves.add(pos1)
                pos1 = i+pos[0], pos[1]-i
                if self.is_place_empty(*pos1):
                    moves.add(pos1)
            for move in self.get_neighbors(*start):
                moves.add(move)
                
            return list(moves)     
            
        to_see = [start, None]
        current_distance = 0
        seen = set()
        while to_see:
            current = to_see.pop(0)
            if current is None:
                current_distance += 1
                if current_distance > max_dist:
                    break
                to_see.append(None)
                continue
            if current in seen:
                continue
            seen.add(current)
            for neighbor in self.get_neighbors(*current):
                if neighbor not in seen:
                    to_see.append(neighbor)
        return list(seen)

    def get_moves(self, start):
        return list(filter(lambda x: not self.contains_mob(*x), self.get_accessible_cases(start)))

    def get_attackable_cases(self, start: tuple[int, int]) -> list[tuple[int, int]]:
        # return self.get_accessible_cases(start, self.get_mob(*start).element)
        return list(filter(lambda x: not self.contains_mob(*x) or self.get_mob(*x).owner != self.turn ,self.get_accessible_cases(start)))

    def get_neighbors(self, i, j):
        neighbors = []
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ni, nj = i + di, j + dj
            if self.is_place_empty(ni, nj):
                neighbors.append((ni, nj))
        return neighbors
