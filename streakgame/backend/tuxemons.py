from enum import Enum
from typing import Optional
from scripts.constants import *
from pygame import Color
import pygame
from streakgame.boring import imgs


class TuxemonType(Enum):
    fire = 1
    water = 2
    ice = 3


all_tuxemons = {
    "snowrilla": TuxemonType.ice,
    "metesaur": TuxemonType.fire,
    "fribbit": TuxemonType.water,
    "eruptibus": TuxemonType.fire,
    "grinflare": TuxemonType.fire,
    "hectapod": TuxemonType.water,
    "qetzlrokilus": TuxemonType.fire,

    "fuzzlet": TuxemonType.ice,
    "fuzzina": TuxemonType.ice,

    "aardorn": TuxemonType.ice,
    "aardart": TuxemonType.ice,

    "agnidon": TuxemonType.fire,
    "agnigon": TuxemonType.fire,

    "cardiling": TuxemonType.fire,
    "cardinale": TuxemonType.fire,

    "noctula": TuxemonType.water,
    "noctalo": TuxemonType.water,
}
default_tuxemons = UNLOCKED_ANKIMONS
[
    "snowrilla",
    "metesaur",
    "fribbit",
    "eruptibus",
    "grinflare",
    "hectapod",
    "qetzlrokilus",
    "fuzzlet",
    "aardorn",
    "agnidon",
    "cardiling",
    "noctula"

]

evolutions = {
    "fuzzlet": "fuzzina",
    "aaardorn": "aardart",
    "agnidon": "agnigon",
    "cardiling": "cardinale",
    "noctula": "noctalo"
}

type_colors: dict[TuxemonType:Color] = {
    TuxemonType.fire: Color("darkred"),
    TuxemonType.water: Color("darkblue"),
    TuxemonType.ice: Color("darkcyan")
}

favorite_fruits: dict[TuxemonType:str] = {
    TuxemonType.fire: "fire fruit",
    TuxemonType.water:"water fruit",
    TuxemonType.ice:  "ice fruit"
}


class Tuxemon:
    counter = 0

    def __init__(self, name):
        self.id = Tuxemon.counter
        Tuxemon.counter += 1
        self.xp: Optional[int] = None
        self.name: Optional[str] = None
        self.imgs: Optional[dict[str, pygame.Surface]] = None
        self.type: Optional[TuxemonType] = None

        self.init_tuxemon(name)
        self.level = 1

    def init_tuxemon(self, name):
        self.xp = 0
        self.name = name
        self.imgs = imgs.load_tuxemon_imgs(name)
        self.favorite_color = (0, 60, 117)

    def max_xp(self):
        return 100 * self.level

    def __repr__(self):
        return f"Tuxemon({self.name})"


    def add_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} xp, total: {self.xp}")
        if self.xp > self.max_xp():
            self.level_up()

    def level_up(self):
        print(f"{self.name} leveled up!")

        print(f"leveling up to level {self.level + 1}, no evolution")
        self.level += 1
        self.xp = 0

    def get_evolution_chain(self):
        return [self]


from streakgame.backend.inventory import Inventory


class TuxemonInventory:
    def __init__(self, inventory: Inventory):
        self.tuxemons: dict[int, Tuxemon] = {}
        self.inventory = inventory

    def add_tuxemon(self, t: Tuxemon):
        self.tuxemons[t.id] = t

    def add_default_tuxemons(self):
        for name in default_tuxemons:
            self.add_tuxemon(Tuxemon(name))

    def feed_tuxemon(self, tuxemon_id: int, index):
        tuxemon = self.tuxemons.get(tuxemon_id)
        if tuxemon:
            nb_remaining = self.inventory.get_food()
            name = list(nb_remaining.keys())[index]
            nb_remaining = nb_remaining[name]
            if  nb_remaining > 0 and tuxemon.xp < tuxemon.max_xp() + 1:
                self.inventory.consume_item(name, 1)
                tuxemon.add_xp(25 if index == 0 else 10 if index == 1 else 5)

        else:
            print(f"no tuxemon with id {tuxemon_id}")

    def dump(self):
        res = {}
        for tuxemon in self.tuxemons.values():
            res[tuxemon.name] = {
                "xp": tuxemon.xp,
                "level": tuxemon.level
            }
        return res

    def load(self, tuxemons: dict):
        for tuxemon_name in tuxemons:
            tuxemon = Tuxemon(tuxemon_name)
            tuxemon.xp = tuxemons[tuxemon_name]["xp"]
            tuxemon.level = tuxemons[tuxemon_name]["level"]

            self.add_tuxemon(tuxemon)

    def __iter__(self):
        return iter(self.tuxemons.values())
