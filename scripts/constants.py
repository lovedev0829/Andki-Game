import os
cwd = os.path.dirname(__file__)
anki_data_path = os.path.join(cwd, "anki_data.json")
TRAINERS = [os.path.join('assets/trainers/',name) for name in os.listdir('assets/trainers/')]
