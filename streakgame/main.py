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

def main():
    geometry = mw.app.primaryScreen().geometry()

    rect = [geometry.x(),geometry.y(),geometry.width(), geometry.height()]
    pygame.init()
    info = pygame.display.Info()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (info.current_w/2 - WIDTH/2,34)
    
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE, vsync=True)
    pygame.display.set_caption('AnkiNick-Mon Farm')
    from streakgame.game import Game
    game = Game(win)
    from streakgame.game import PlantSpot
    from streakgame.backend.tuxemons import Tuxemon
    PlantSpot.counter = 0  # reset class counter (used as id) there is probably a better way to do this
    Tuxemon.counter = 0
    
    game.run()
    pygame.quit()
        

if __name__ == "__main__":
    main()
