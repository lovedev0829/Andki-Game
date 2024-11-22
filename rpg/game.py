import time 
import copy
import random
from rpg.engine import Engine
from rpg.tmx import Pytmx
import pygame
import pickle 



class Game:
    def __init__(self) -> None:
        self.move = 0
        self.learn = True
        self.data = [{},{}]
        self.cards_learned = [0,0]
        

    def add_data(self, data:str, player_count):
        self.data[int(player_count)]['trainer']  =  data['trainer']
        self.data[int(player_count)]['ankimons']  = data['ankimons']
    
    def init_game(self):
        self.engine = Engine(Pytmx(pygame.Surface((0,0))).free_places, self.data[0]['ankimons'].copy().update(self.data[1]["ankimons"]), pygame.Surface((0,0)), Pytmx(pygame.Surface((0,0))), [self.data[i]['trainer'] for i in range(2)])

    def get_turn(self):
        return self.move % 2
    
    def copy(self):
        g = Game()
        g.data = copy.deepcopy(self.data)
        return 