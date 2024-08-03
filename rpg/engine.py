from enum import Enum
from typing import Optional
import images
from rpg.ParticleSystem import EffectManager, Fire
import pygame
from pygame import Color
import logging

logging.basicConfig()

# logging.root.setLevel(logging.NOTSET)

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger('game')

MAX_MOVE_DISTANCE = 3


class Mob:
    def __init__(self, i, j, name, element, owner: "Player", screen):
        self.i = i
        self.j = j
        self.name = name
        self.element = element
        self.img = self.load_image()
        self.health = 100
        self.dmg = 10
        self.screen = screen
        self.manager = EffectManager(self.screen)
        self.owner = owner
    
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
        mob.lost_health(self.dmg*multiplier)

    def lost_health(self, dmg):
        self.health = max(0, self.health - dmg)
        if self.health == 0:
            self.owner = None

    def draw(self, map_t):
        x, y = map_t.ortho_to_iso(self.j, self.i)
        self.manager.update()
        
        if self.element.lower() == 'fire':
            self.manager.add_particle(Fire, (x, y+10))
        self.screen.blit(self.img, (x - 32, y - 24))
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
    def __init__(self, free_places, ankimons: dict, screen):
        self.turn: Player = Player.Player1
        self.free_places: list[tuple[int, int]] = free_places  # List of (i, j) tuples
        self.player1_mobs: list[Mob] = []
        self.player2_mobs: list[Mob] = []
        names = list(ankimons.keys())
        if ankimons:
            self.add_mob(Mob(24, 21, names[0], ankimons[names[0]], Player.Player1, screen))
            self.add_mob(Mob(25, 21, names[1], ankimons[names[1]], Player.Player1, screen))
            self.add_mob(Mob(26, 21, names[2], ankimons[names[2]], Player.Player1, screen))
            self.add_mob(Mob(17, 24, names[0], ankimons[names[0]], Player.Player2, screen))
            self.add_mob(Mob(18, 24, names[1], ankimons[names[1]], Player.Player2, screen))
            self.add_mob(Mob(19, 24, names[2], ankimons[names[2]], Player.Player2, screen))

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
        if start == end: return False
        if not self.is_place_empty(*end):
            logger.debug("End place is not empty")
            return False
        if (end[0], end[1]) not in self.get_moves((start[0], start[1])):
            logger.debug("End place is not accessible")
            return False
        mob.move(*end)
        neighbors = filter(lambda x: self.contains_mob(*x) and self.get_mob(*x).owner != self.turn, self.get_neighbors(*end))
        for neighbor in neighbors:
            self.get_mob(*neighbor).attack(mob)
        self.switch_turn()
        return True

    def perform_attack(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        logger.debug(f"Trying to attack from {start} to {end}")
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
        attacker.attack(defender)
        if defender.health <= 0:
            if defender in self.player1_mobs:
                self.player1_mobs.remove(defender)
            else:
                self.player2_mobs.remove(defender)
        self.switch_turn()
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
