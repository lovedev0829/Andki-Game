import pygame
import os
from aqt import mw
from aqt.qt import *
from rpg.config import config
from scripts.constants import TRAINERS
import time
import ctypes
from scripts.utils import center_widget
from rpg.engine import Trainer
import random
import json
ctypes.windll.shcore.SetProcessDpiAwareness(1)



def mainloop(ankimons, loadsave=False):
    pygame.quit()
    pygame.init()
    info = pygame.display.Info()
    size = info.current_w,info.current_h
    yoffset = 27

    trainers = [Trainer(TRAINERS[0], 1, 1), Trainer(random.choice(TRAINERS), 1, 1)]
    mw.window().setGeometry(0,yoffset,size[0]/2,size[1]-yoffset*2.3)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (size[0]/2,yoffset)
    from rpg.ankirpg import AnkiRPG, data_path
    
    pygame.mixer.music.stop()
    pygame.display.set_caption("AnkiRPG")
    
    win = pygame.display.set_mode((size[0]/2,size[1]-yoffset*2.3), pygame.DOUBLEBUF | pygame.HWSURFACE|pygame.RESIZABLE)
    chess = AnkiRPG(win, ankimons, trainers, loadsave).run()
    

if __name__ == '__main__':
    mainloop()
