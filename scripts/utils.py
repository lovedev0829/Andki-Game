import datetime
import json
import os
import aqt
from aqt import mw
import base64
import aqt.overview
from scripts.constants import anki_data_path

cwd = os.path.dirname(os.path.dirname(__file__))
# requires arguments a, b, c because of how Anki calls the hook
def process_file(a, b, c):
    # get today's ordinal date
    today_ordinal = datetime.date.today().toordinal()
    anki_data = json.load(open(anki_data_path))
    if 'trainer_xp' in anki_data:
        anki_data['trainer_xp'] += 1
    else:
        anki_data['trainer_xp'] = 1
    if "time_ordinal" not in anki_data or anki_data["time_ordinal"] != today_ordinal:
        anki_data["time_ordinal"] = today_ordinal
        anki_data["nb_cards_learned_today"] = 1
    else:
        anki_data["nb_cards_learned_today"] += 1
    if 'moves' not in anki_data:
        anki_data['moves'] = anki_data['nb_cards_learned_today']
        json.dump(anki_data, open(anki_data_path, 'w'))
    else:
        anki_data['moves'] += 0.1
    

    json.dump(anki_data, open(anki_data_path, "w"))

def xp_to_lvl(xp:int):
    count = 0
    for i in range(100):
        count += 50*pow(2,i//10)
        if count >= xp:
            return i+1 + (count - xp)/50*pow(2,i//10)
        print(count)    

def change_data(data, value):
    anki_data = json.load(open(anki_data_path))
    anki_data[data] = value
    json.dump(anki_data, open(anki_data_path,'w'))

def add_data(data, value):
    anki_data = json.load(open(anki_data_path))
    if data not in anki_data:
        anki_data[data] = value
    json.dump(anki_data, open(anki_data_path,'w'))
def get_data() -> dict:
    return json.load(open(os.path.join(os.getcwd(),anki_data_path), 'r'))

def get_html(image, message):
    return f"""
    <style>
        body {{
            text-align: center;
        }}    
        .image-button {{
            background-color: transparent;
            cursor: pointer;
        }}

        .image-button img {{
            align-content: center;
            width: 504px;  /* Adjust the size as needed */
            height: 250px; /* Adjust the size as needed */
        }}    
    </style>
    <button class="image-button" onclick="pycmd('{message}')">
        <img src="{image}" alt="gif">
    </button>
    """

def center_widget(widget):
    window_size = widget.geometry().size()
    window_size = [window_size.width(), window_size.height()]    
    screen_size = mw.app.primaryScreen().size() 
    screen_size = [screen_size.width(), screen_size.height()]
    widget.setGeometry(screen_size[0]//2-window_size[0]//2, screen_size[1]//2-window_size[1]//2, *window_size)

def add_msg_to_db(msg):
    if not os.path.exists(anki_data_path):
        with open(anki_data_path, "w") as f:
            f.write("[]")
    with open(anki_data_path, "r") as f:
        data = json.load(f)
    try:
        data.append(msg)
    except Exception:
        print('couldnt add message to database')
    with open(anki_data_path, "w") as f:
        json.dump(data, f)
started = False
def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/gif;base64,{encoded_string}"
# Inject a button in the deck view
def add_btn(
        deck_browser: "aqt.overview.Overview", 
        content: "aqt.overview.OverviewContent",
) -> None:
    path = os.path.join(cwd, f"assets", "ui","Chess.gif")
    content.table += get_html(image_to_base64(path), "start_rpg")

class manager:
    def __init__(self) -> None:
        self.Frame = 50
        self.SIZE = [500,200]
        self.buf = 5
        self.buffer_size = 100        