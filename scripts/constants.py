import os
import json
cwd = os.path.dirname(__file__)
anki_data_path = os.path.join(os.path.dirname(cwd) ,"anki_data.json")
cwd = os.path.dirname(cwd)

TRAINERS = [os.path.join(cwd,f'assets/trainers/{name}') for name in os.listdir(os.path.join(cwd,f'assets/trainers/'))]
ANKIMONS = ["AnkiNick","Beekeeper Alder King","Primus Nephritico","Silver Globe Knight","Chrome-coated info soap","Immune Shield Globe Knight","Icy Gold Pastor","Illuminated goblin","Ancient evergreen reactor","Tent landlord Hedgehog Moon","Plump Bell Ogre","Clever Maasai Gold Net Warrior","Diamond Ninja Messenger","Glowing Net Knight"]

