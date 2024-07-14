import datetime
import json
import os
import aqt
from aqt import mw
from scripts.constants import anki_data_path


# requires arguments a, b, c because of how Anki calls the hook
def process_file(a, b, c):
    # get today's ordinal date
    today_ordinal = datetime.date.today().toordinal()
    anki_data = json.load(open(anki_data_path))

    if "time_ordinal" not in anki_data or anki_data["time_ordinal"] != today_ordinal:
        anki_data["time_ordinal"] = today_ordinal
        anki_data["nb_cards_learned_today"] = 1
    else:
        anki_data["nb_cards_learned_today"] += 1
    
    json.dump(anki_data, open(anki_data_path, "w"))

def change_data(data, value):
    anki_data = json.load(open(anki_data_path))
    if data in anki_data:
        anki_data[data] = value
    json.dump(anki_data, open(anki_data_path,'w'))

def add_data(data, value):
    anki_data = json.load(open(anki_data_path))
    if data not in anki_data:
        anki_data[data] = value
    json.dump(anki_data, open(anki_data_path,'w'))
def get_data() -> dict:
    return json.load(open(os.path.join(os.getcwd(),anki_data_path), 'r'))

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
    data.append(msg)
    with open(anki_data_path, "w") as f:
        json.dump(data, f)

# Inject a button in the deck view
def add_btn(
        deck_browser: "aqt.overview.Overview", 
        content: "aqt.overview.OverviewContent",
) -> None:
    import bs4
    soup = bs4.BeautifulSoup(content.table, "html.parser")
    # add a button called "Start learning with AnkiRPG"
    btn = soup.new_tag("button")
    btn["class"] = "btn"
    btn.string = "Start learning with AnkiNick-Mon."
    # hook
    btn["onclick"] = "pycmd('start_rpg');pycmd('study');"
    soup.append(btn)
    content.table = str(soup)
