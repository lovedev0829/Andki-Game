from enum import Enum
from typing import Optional
import images

import pygame
from pygame import Color
import logging

logger = logging.getLogger(__name__)

MAX_MOVE_DISTANCE = 3


class Mob:
    def __init__(self, i, j, name, element, owner: "Player"):
        self.i = i
        self.j = j
        self.name = name
        self.element = element
        self.img = images.load_mob_img(name)
        self.health = 100
        self.dmg = 10
        self.owner = owner

    def move(self, i, j):
        self.i = i
        self.j = j

    def attack(self, mob: "Mob"):
        mob.lost_health(self.dmg)

    def lost_health(self, dmg):
        self.health = max(0, self.health - dmg)
        if self.health == 0:
            self.owner = None

    def draw(self, win, map_t):
        x, y = map_t.ortho_to_iso(self.j, self.i)
        win.blit(self.img, (x - 32, y - 24))
        # Health bar ally
        if self.owner == Player.Player1:
            pygame.draw.rect(win, Color("red"), (x - 16, y - 16, 32, 4))
            pygame.draw.rect(win, Color("green"), (x - 16, y - 16, 32 * self.health / 100, 4))
        else:
            pygame.draw.rect(win, Color("black"), (x - 16, y - 16, 32, 4))
            pygame.draw.rect(win, Color("red"), (x - 16, y - 16, 32 * self.health / 100, 4))


class Player(Enum):
    Player1 = 1
    Player2 = 2


class Mode(Enum):
    Idle = 0
    Move = 1
    Attack = 2


class Engine:
    def __init__(self, free_places, ankimons: dict):
        self.turn: Player = Player.Player1
        self.free_places: list[tuple[int, int]] = free_places  # List of (i, j) tuples
        self.player1_mobs: list[Mob] = []
        self.player2_mobs: list[Mob] = []
        names = list(ankimons.keys())
        self.add_mob(Mob(17, 21, names[0], ankimons[names[0]], Player.Player1))
        self.add_mob(Mob(18, 21, names[1], ankimons[names[1]], Player.Player1))
        self.add_mob(Mob(19, 21, names[2], ankimons[names[2]], Player.Player1))

        self.add_mob(Mob(17, 24, names[0], ankimons[names[0]], Player.Player2))
        self.add_mob(Mob(18, 24, names[1], ankimons[names[1]], Player.Player2))
        self.add_mob(Mob(19, 24, names[2], ankimons[names[2]], Player.Player2))

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
        return (j, i) in self.free_places and not self.contains_mob(i, j)

    def get_mob(self, i: int, j: int) -> Optional[Mob]:
        for mob in self.player1_mobs + self.player2_mobs:
            if mob.i == i and mob.j == j:
                return mob
        return None

    def perform_move(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        logger.debug(f"Trying to move from {start} to {end}")
        mob = self.get_mob(*start)

        if not self.is_place_empty(*end):
            logger.debug("End place is not empty")
            return False
        if (end[0], end[1]) not in self.get_accessible_cases((start[0], start[1]), mob.element):
            logger.debug("End place is not accessible")
            return False
        mob.move(*end)
        self.switch_turn()
        return True

    def perform_attack(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        logger.debug(f"Trying to attack from {start} to {end}")
        attacker = self.get_mob(*start)
        defender = self.get_mob(*end)

        if attacker.owner == defender.owner:
            logger.debug("Can't attack an ally")
            return False
        if (end[0], end[1]) not in self.get_attackable_cases((start[0], start[1])):
            logger.debug("End place is not accessible")
            return False
        attacker.attack(defender)
        self.switch_turn()
        return True

    def switch_turn(self):
        self.turn = Player.Player1 if self.turn == Player.Player2 else Player.Player2

    def get_all_mobs(self):
        return self.player1_mobs + self.player2_mobs

    def get_accessible_cases(self, start: tuple[int, int], element:str) -> list[tuple[int, int]]:
        element = element.lower()
        if element == 'fire':
            max_dist = 2
        else:
            max_dist = 3
        def get_neighbors(i, j):
            neighbors = []
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                ni, nj = i + di, j + dj
                if self.is_place_empty(ni, nj):
                    neighbors.append((ni, nj))
            return neighbors

        moves = set()
        pos = start
        if element == 'water':
            for i in range(-max_dist, max_dist+1):
                if self.is_place_empty(i+pos[0], pos[1]):
                    moves.add((i+pos[0],pos[1]))
                if self.is_place_empty(pos[0], i+pos[1]):
                    print(pos[0], i+pos[1])
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
            for neighbor in get_neighbors(*current):
                if neighbor not in seen:
                    to_see.append(neighbor)
        return list(seen)

    def get_attackable_cases(self, start: tuple[int, int]) -> list[tuple[int, int]]:
        def get_neighbors(i, j):
            neighbors = []
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                ni, nj = i + di, j + dj
                if self.contains_mob(ni, nj):
                    neighbors.append((ni, nj))
            return neighbors

        return get_neighbors(*start)
