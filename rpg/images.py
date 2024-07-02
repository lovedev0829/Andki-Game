import pygame
import os

cwd = os.path.dirname(__file__)


def load_mob_img(name):
    return pygame.image.load(os.path.join(cwd, "assets", "tuxemons", f"{name}-front.png")).convert_alpha()
