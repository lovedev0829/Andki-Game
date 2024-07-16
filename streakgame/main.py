import os
import sys

from streakgame.boring.config import WIDTH, HEIGHT
import logging
import pygame

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO, filename="game.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
game = None
def main(stats):
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

def mainnowin(stats):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-2000,-2000)
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HIDDEN, vsync=True)
    from streakgame.game import GameNoWindow
    global game
    game = GameNoWindow(win,stats)
    

    from streakgame.game import PlantSpot
    from streakgame.backend.tuxemons import Tuxemon
    PlantSpot.counter = 0  # reset class counter (used as id) there is probably a better way to do this
    Tuxemon.counter = 0
    
    game.run()
        

if __name__ == "__main__":
    main()
