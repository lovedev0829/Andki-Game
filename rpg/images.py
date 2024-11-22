import pygame
import os

cwd = os.path.dirname(__file__)

print(cwd)
def load_mob_img(name):
    return pygame.transform.scale(pygame.image.load(os.path.join(cwd, "assets", "tuxemons", f'{name}.png')).convert_alpha(),(64,64))