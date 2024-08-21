import pygame
import os
from aqt import mw
from aqt.qt import *
from rpg.config import config
from scripts.constants import TRAINERS, ANKIMONS, STATS
import time
import ctypes
from scripts.utils import center_widget, xp_to_lvl, get_data
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
    from rpg.ankirpg import AnkiRPG, data_path
    trainer_name = json.load(open(data_path, 'r'))['default_trainer']
    for i in range(10):
        bot_trainer = random.choice(list(STATS.keys()))
        print(bot_trainer)
    default_stats = [1,1,0]
    # num = (int(xp_to_lvl(get_data().get('trainer_xp', 0)))//2)
    # default_stats[0] += num * 0.1
    # default_stats[1] += num * 0.1

    trainers = [Trainer(trainer_name, *default_stats), Trainer(bot_trainer ,*STATS[bot_trainer])]
    mw.window().setGeometry(0,yoffset,size[0]/2,size[1]-yoffset*2.3)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (size[0]/2,yoffset)
    
    
    pygame.mixer.music.stop()
    pygame.display.set_caption("AnkiRPG")
    
    win = pygame.display.set_mode((size[0]/2,size[1]-yoffset*2.3), pygame.DOUBLEBUF | pygame.HWSURFACE|pygame.RESIZABLE)
    chess = AnkiRPG(win, ankimons, trainers, loadsave).run()
    

if __name__ == '__main__':
    mainloop()
