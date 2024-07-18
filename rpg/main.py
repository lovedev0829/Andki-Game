import pygame
import os
from aqt import mw
from rpg.config import config
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def mainloop():
    pygame.init()
    info = pygame.display.Info()
    size = info.current_w,info.current_h
    mw.window().setGeometry(0,0,size[0]/2,size[1])

    # os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (rect[0]+rect[2]/2,rect[1]+rect[3]/2)
    
    pygame.mixer.music.stop()
    pygame.display.set_caption("AnkiRPG")
    from rpg.ankirpg import AnkiRPG
    win = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE|pygame.RESIZABLE)
    AnkiRPG(win).run()


if __name__ == '__main__':
    mainloop()
