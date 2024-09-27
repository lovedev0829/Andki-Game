import datetime
import json
import time
import os
import aqt
from aqt import mw
import base64
import aqt.overview
import aqt.reviewer
from scripts.constants import anki_data_path
from scripts.notification import Notification
import math
import pygame

cwd = os.path.dirname(os.path.dirname(__file__))
# requires arguments a, b, c because of how Anki calls the hook
def process_file(a:aqt.reviewer.Reviewer, b, c):
    # get today's ordinal date
    
    today_ordinal = datetime.date.today().toordinal()
    anki_data = json.load(open(anki_data_path))
    if hasattr(mw, 'win'):
        if hasattr(mw.win, 'update'):
            mw.win.update()
        print( hasattr(mw.win, 'required_cards') , hasattr(mw.win, 'completed_cards'))
        if hasattr(mw.win, 'required_cards') and hasattr(mw.win, 'completed_cards'):
            encouragement = ""
            html = f"""\
        <table cellpadding=10>
        <tr>
        <center><b>{mw.win.completed_cards+1}/{mw.win.required_cards} cards done so far!</b><br>
        {encouragement}</center>
        </td>
        </tr>
        </table>"""
            
            palette = mw.palette()
            notification = Notification(
                html,
                mw.progress,
                duration=2,
                parent=mw.app.activeWindow() or mw,
                align_horizontal='left',
                align_vertical='bottom',
                space_horizontal=mw.window().geometry().width()/20,
                space_vertical=mw.window().geometry().height()/5,
                # bg_color=palette.color(mw.backgroundRole()),
            )

            notification.show()

    if 'trainer_xp' in anki_data:
        anki_data['trainer_xp'] += 1
        prize()

        
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
def activate_full_screen():
    pygame.init()
    info = pygame.display.Info()
    global screen_size
    screen_size = [info.current_w, info.current_h]
    mw.window().setGeometry(10,60,info.current_w,info.current_h-70)

def area_until_x(x):
    """Calculate the area under the curve from x=0 to a given x."""
    n = math.floor(x / 10)
    # Sum the areas for all complete intervals before the current interval
    area = sum(2**i * 50 * 10 for i in range(n))
    # Add the partial area for the current interval
    area += (x - n * 10) * (2**n * 50)
    return area

def xp_to_lvl(xp):
    """Find the x value where the area under the curve equals xp."""
    x = 0
    # Incrementally increase x until the area under the curve equals xp
    while area_until_x(x) < xp:
        x += 0.01  # Increase x by small increments for better precision
    return x
def convert_float_to_int_if_possible(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def prize():
    xp = get_data().get('trainer_xp', 1)
    if xp_to_lvl(xp) % 1 == 0:
        1
def change_data(data, value):
    anki_data = json.load(open(anki_data_path))
    anki_data[data] = value
    json.dump(anki_data, open(anki_data_path,'w'))

def add_data(data, value):
    anki_data = json.load(open(anki_data_path))
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
    mw.web.eval('x=2;')
    path = os.path.join(cwd, f"assets", "ui","Chess.gif")
    content.table += get_html(image_to_base64(path), "start_rpg")
    

class manager:
    def __init__(self) -> None:
        self.Frame = 50
        self.SIZE = [500,200]
        self.buf = 5
        self.buffer_size = 100        