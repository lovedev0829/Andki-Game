import os
cwd = os.path.dirname(__file__)
anki_data_path = os.path.join(os.path.dirname(cwd) ,"anki_data.json")
cwd = os.path.dirname(cwd)

TRAINERS = [os.path.join(cwd,f'assets/trainers/{name}') for name in os.listdir(os.path.join(cwd,f'assets/trainers/'))]

