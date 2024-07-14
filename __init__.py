from __future__ import annotations
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
import streakgame.main
from rpg.main import mainloop
from scripts.utils import process_file, add_msg_to_db, add_btn, center_widget
import asyncio, time
from scripts.popups import rpg_popup, trainer_challenge, trainer_popup, attribute_popup
from aqt.deckbrowser import DeckBrowser
from aqt.webview import WebContent

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
# aqt.gui_hooks.
# Add a button to the main screen with title "start game" and that starts the game when clicked
pygame_surf = None
def start_game():
    global pygame_instace
    pygame_instace = streakgame.main.mainnowin()
    

def start_rpg():
    global pygame_instace
    mw.win = win = QMainWindow()
    ui = trainer_popup(win)
    
    

    pygame_instace = mainloop()
def on_profile_open():
    
    mw.win = win = QMainWindow()
    attribute_popup(win)
    due_tree = mw.col.sched.deck_due_tree()
    to_review = due_tree.review_count + due_tree.learn_count + due_tree.new_count
    if to_review:
        aqt.utils.showInfo(f"You have {to_review} cards to learn today. Good luck !")
    
    data = json.load(open(anki_data_path, 'r'))
    data['nb_cards_to_review_today'] = to_review
    json.dump(data, open(anki_data_path, "w"))
    # center_widget(mw.menuWidget())
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
def on_webview_will_set_content(
    web_content: WebContent, context: object | None) -> None:
    if not isinstance(context, DeckBrowser):
        return
    path = os.path.join(os.getcwd(),"assets/Dragonride_front_blue.png")
    print(path)
    web_content.body += '''
<img img="image.png" id="counter";">
<script>
setInterval(() => {
    document.getElementById("counter").src = "'''+path+'''";
}, 1000);</script>
'''
print(os.getcwd())

# gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
