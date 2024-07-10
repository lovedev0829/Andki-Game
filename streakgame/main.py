import os
import sys

from streakgame.boring.config import WIDTH, HEIGHT
import logging
import pygame

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO, filename="game.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def main(showwin=True):
    pygame.init()
    
    if showwin:
        win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE, vsync=True)
        pygame.display.set_caption("AnkiStreak")
        from streakgame.game import Game
        game = Game(win)
        from streakgame.game import PlantSpot
        from streakgame.backend.tuxemons import Tuxemon
        PlantSpot.counter = 0  # reset class counter (used as id) there is probably a better way to do this
        Tuxemon.counter = 0
        
        game.run()
        pygame.quit()
    else:
        pass

if __name__ == "__main__":
    main()
