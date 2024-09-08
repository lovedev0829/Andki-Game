import pygame
import os

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

class Animation:
    def __init__(self, images, dur=5, loop=True):
        self.images = images
        self.dur = dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def reset(self):
        self.frame = 0

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
        dirs[dire] = [Animation(load_images(os.path.join(path ,dire, child_dir),size=size), dur=4) for child_dir in os.listdir(os.path.join(path ,dire))]
    return dirs
