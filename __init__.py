import datetime
import json
import os.path
import sys
sys.path.append(os.path.dirname(__file__))
import threading
import aqt.utils
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from aqt import gui_hooks, mw
from aqt.qt import * 
from PyQt5.QtOpenGL import QGLWidget
import streakgame.main
from rpg.main import mainloop

cwd = os.path.dirname(__file__)

anki_data_path = os.path.join(cwd, "anki_data.json")

# Inject a button in the deck view
def add_btn(
        deck_browser: "aqt.overview.Overview", 
        content: "aqt.overview.OverviewContent",
) -> None:
    import bs4
    soup = bs4.BeautifulSoup(content.table, "html.parser")
    # add a button called "Start learning with AnkiRPG"
    print(soup.contents)
    btn = soup.new_tag("button")
    btn["class"] = "btn"
    btn.string = "Start learning with AnkiNick-Mon."
    # hook
    btn["onclick"] = "pycmd('start_rpg');pycmd('study');"
    soup.append(btn)
    content.table = str(soup)


def add_msg_to_db(msg):
    if not os.path.exists(anki_data_path):
        with open(anki_data_path, "w") as f:
            f.write("[]")
    with open(anki_data_path, "r") as f:
        data = json.load(f)
    data.append(msg)
    with open(anki_data_path, "w") as f:
        json.dump(data, f)


started = False


def bridge(handled, message: str, context):
    global started
    print("Bridge", message)
    if message == "start_rpg":
        if not started:
            threading.Thread(target=start_rpg, daemon=True).start()
            started = True
    if message in ["ease1", "ease2", "ease3", "ease4"]:
        add_msg_to_db(message)
    return handled

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

aqt.gui_hooks.overview_will_render_content.append(add_btn)
aqt.gui_hooks.webview_did_receive_js_message.append(bridge)

# Add a button to the main screen with title "start game" and that starts the game when clicked
def start_game():
    streakgame.main.main()

def start_rpg():
    mainloop()

class GLWidget(QGLWidget):  # Change to QGLWidget for broader compatibility
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)    
def on_profile_open():


    due_tree = mw.col.sched.deck_due_tree()
    to_review = due_tree.review_count + due_tree.learn_count + due_tree.new_count
    if to_review:
        aqt.utils.showInfo(f"You have {to_review} cards to learn today. Good luck !")

    json.dump({"nb_cards_to_review_today": to_review}, open(anki_data_path, "w"))
    try:
        start_game()
    except pygame.error as e:
        print(e)
        

gui_hooks.profile_did_open.append(on_profile_open)
gui_hooks.reviewer_did_answer_card.append(process_file)

action = aqt.qt.QAction("Start game", mw)
action.triggered.connect(start_game)
mw.form.menuTools.addAction(action)

rpg = aqt.qt.QAction("Start rpg", mw)
rpg.triggered.connect(start_rpg)
mw.form.menuTools.addAction(rpg)
