import os
import json
cwd = os.path.dirname(__file__)
anki_data_path = os.path.join(os.path.dirname(cwd) ,"anki_data.json")
streak_data_path = os.path.join(os.path.dirname(cwd) ,"streakgame", "game_data", 'tuxemon.json')
cwd = os.path.dirname(cwd)

DATA:dict = json.load(open(anki_data_path, 'r'))

TRAINERS = [name.replace('.png','') for name in os.listdir(os.path.join(cwd,f'assets/trainers/'))]
ITEMS = [name.replace('.png','') for name in os.listdir(os.path.join(cwd,f'assets/items/'))]
SAVE_PATH = os.path.join(cwd, 'rpg','game.save')
ANKIMONS = ["AnkiNick","Beekeeper Alder King","Primus Nephritico","Silver Globe Knight","Chrome-coated info soap","Immune Shield Globe Knight","Icy Gold Pastor","Illuminated goblin","Ancient evergreen reactor","Tent landlord Hedgehog Moon","Plump Bell Ogre","Clever Maasai Gold Net Warrior","Diamond Ninja Messenger","Glowing Net Knight"]
UNLOCKED_ANKIMONS = DATA.get('Unlocked_Ankimons', None) or ANKIMONS
trainer_xp = DATA.get('Trainer_xp', 0)
STATS = {'Scientist': [0.8, 0.8, 1],'Alchemist': [1.4, 0.7, 0], 'Dragon': [1.2, 1.2, 0],'Farmer': [1.0, 1.5, 0], 'Ninja': [1.6, 0.5, 1]}
