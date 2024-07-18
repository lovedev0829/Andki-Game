import os
import sys
from streakgame.boring.config import WIDTH, HEIGHT
import logging
import pygame
from aqt import mw
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO, filename="game.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
game = None
def main(stats):
    geometry = mw.app.primaryScreen().geometry()

    rect = [geometry.x(),geometry.y(),geometry.width(), geometry.height()]
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (rect[0]+rect[2]/2,rect[1]+rect[3]/2)
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE, vsync=True)
    pygame.display.set_caption("AnkiStreak")
    from streakgame.game import Game
    game = Game(win,stats)
    from streakgame.game import PlantSpot
    from streakgame.backend.tuxemons import Tuxemon
    PlantSpot.counter = 0  # reset class counter (used as id) there is probably a better way to do this
    Tuxemon.counter = 0
    
    game.run()
    pygame.quit()
        

if __name__ == "__main__":
    main()
