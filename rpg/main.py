import pygame

from rpg.config import config
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def mainloop():
    pygame.init()
    pygame.mixer.music.stop()
    pygame.display.set_caption("AnkiRPG")
    from rpg.ankirpg import AnkiRPG
    win = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE|pygame.RESIZABLE)
    AnkiRPG(win).run()


if __name__ == '__main__':
    mainloop()
