import pygame
import os
from aqt import mw
from rpg.config import config
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def mainloop():
    pygame.quit()
    pygame.init()
    info = pygame.display.Info()
    size = info.current_w,info.current_h
    yoffset = 27
    mw.window().setGeometry(0,yoffset,size[0]/2,size[1]-yoffset*2.3)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (size[0]/2,yoffset)
    
    pygame.mixer.music.stop()
    pygame.display.set_caption("AnkiRPG")
    from rpg.ankirpg import AnkiRPG
    win = pygame.display.set_mode((size[0]/2,size[1]-yoffset*2.3), pygame.DOUBLEBUF | pygame.HWSURFACE|pygame.RESIZABLE)
    AnkiRPG(win).run()


if __name__ == '__main__':
    mainloop()
