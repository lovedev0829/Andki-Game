import datetime
import json
import os.path
import sys
sys.path.append(os.path.dirname(__file__))
import threading
import aqt.utils
import pygame
from aqt import gui_hooks, mw
from aqt.qt import * 
from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget
import streakgame.main
from rpg.main import mainloop
from scripts.utils import process_file, add_msg_to_db, add_btn
import asyncio, time
from scripts.popups import rpg_popup
cwd = os.path.dirname(__file__)

anki_data_path = os.path.join(cwd, "anki_data.json")
size = [300,300]


started = False


def bridge(handled, message: str, context):
    global started
    if message == "start_rpg":
        if not started:
            threading.Thread(target=start_rpg, daemon=True).start()
            started = True
    if message in ["ease1", "ease2", "ease3", "ease4"]:
        add_msg_to_db(message)
    return handled


aqt.gui_hooks.overview_will_render_content.append(add_btn)
aqt.gui_hooks.webview_did_receive_js_message.append(bridge)

# Add a button to the main screen with title "start game" and that starts the game when clicked
def start_game():
    global pygame_instace
    pygame_instace = streakgame.main.main(showwin=False)

def start_rpg():
    global pygame_instace
    choose_option = QMainWindow()
    
    ui = rpg_popup()
    print(1)
    ui.setupUi(choose_option)
    print(2)
    choose_option.showNormal()
    print(3)
    mw.win = choose_option
    print(4)

    pygame_instace = mainloop()

def on_profile_open():

    
    # gl = QGLWidget()
    # gl.show()
    due_tree = mw.col.sched.deck_due_tree()
    to_review = due_tree.review_count + due_tree.learn_count + due_tree.new_count
    if to_review:
        aqt.utils.showInfo(f"You have {to_review} cards to learn today. Good luck !")

    json.dump({"nb_cards_to_review_today": to_review}, open(anki_data_path, "w"))
    try:
        start_game()
    except pygame.error as e:
        print(e)


pygame_instace = None
gui_hooks.profile_did_open.append(on_profile_open)
gui_hooks.reviewer_did_answer_card.append(process_file)


action = aqt.qt.QAction("Start game", mw)
action.triggered.connect(start_game)
mw.form.menuTools.addAction(action)

rpg = aqt.qt.QAction("Start rpg", mw)
rpg.triggered.connect(start_rpg)
mw.form.menuTools.addAction(rpg)
