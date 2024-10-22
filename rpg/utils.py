import pygame
import os
import math
from scripts.utils import get_data

def throw(p1, p2, ratio, heigth=0):
    x_dist = p1[0] - p2[0]
    y_dist = p1[1] - p2[1]
    offsets = []
    offsets.append(-x_dist*ratio)
    
    offsets.append(-y_dist*ratio+math.sin(ratio*math.pi)*heigth)
    return offsets

def load_image(path,size=None):
    if size:
        img = pygame.transform.scale(pygame.image.load(path).convert_alpha(),size)
    else:
        img = pygame.image.load(path).convert_alpha()
    return img

def load_images(path,size=None):
    images = []
    for img_name in sorted(os.listdir(path)):
        images.append(load_image(path + '/' + img_name,size=size))
    return images

def get_enclosing_rect(rect_list):
    if not rect_list:
        raise ValueError("The list of rectangles is empty.")
    
    # Use the first rectangle as the base
    enclosing_rect = rect_list[0].copy()
    
    # Union the remaining rectangles with the base
    for rect in rect_list[1:]:
        enclosing_rect.union_ip(rect)
    
    return enclosing_rect

def handle_item(game, engine):
    item = get_data().get('indicies')[1]
    if item == 0:
        for mob in engine.player1_mobs:
            mob.dmg *= 1.1
    if item == 1:
        for mob in engine.player1_mobs:
            mob.defense *= 1.1
    if item == 2:
        engine.player1_mobs[0].trainer.movement += 1
    if item == 3:
        for mob in engine.player1_mobs:
            if mob.element.lower() == 'water':mob.dmg *= 1.3
    if item == 4:
        for mob in engine.player1_mobs:
            if mob.element.lower() == 'fire':mob.dmg *= 1.3
    if item == 5:
        for mob in engine.player1_mobs:
            if mob.element.lower() == 'ice':mob.dmg *= 1.3
    if item == 6:
        for mob in engine.player1_mobs:
            mob.dmg *= 1.2
    if item == 7:
        for mob in engine.player1_mobs:
            mob.defense *= 1.2
    if item == 8:
        game.wild_ankimon_chance += 0.1
    if item == 9:
        engine.player1_mobs[0].trainer.movement += 2
    
class Animation:
    def __init__(self, images, dur=5, loop=True):
        self.images = images
        self.dur = dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def reset(self):
        self.frame = 0
        self.done = False

    def copy(self):
        return Animation(self.images, self.dur, self.loop)
    
    def update(self):
        if not self.done:
            if self.loop:
                self.frame = (self.frame + 1) % (self.dur * len(self.images))
            else:
                self.frame = min(self.frame + 1 ,self.dur * len(self.images) -1)
                if self.frame >= self.dur * len(self.images) -1:
                    self.done = True
        
    
    def img(self):
        return self.images[int(self.frame/self.dur)]


def load_dir(path, size=None):
    dirs = {}
    for dire in sorted(os.listdir(path)):
        dirs[dire] = [Animation(load_images(os.path.join(path ,dire, child_dir),size=size), dur=30//len(load_images(os.path.join(path ,dire, child_dir),size=size)), loop=i==1) for i, child_dir in enumerate(os.listdir(os.path.join(path ,dire)))]
    return dirs
