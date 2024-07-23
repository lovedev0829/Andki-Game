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
from scripts.utils import process_file, add_msg_to_db, add_btn, center_widget, manager
import asyncio, time
from scripts.popups import rpg_popup, trainer_challenge, trainer_popup, attribute_popup
from aqt.deckbrowser import DeckBrowser
from aqt.webview import WebContent


#global vars
cwd = os.path.dirname(__file__)

anki_data_path = os.path.join(cwd, "anki_data.json")
size = [300,300]
button = None
started = False
stats = manager()

def bridge(handled, message: str, context):
    global started
    if message == "start_rpg":
            start_rpg()
    if message == "attribute":
        mw.win = QMainWindow()
        from scripts import utils
        attribute_popup(mw.win, True if utils.started else False)
    if message == "update_streak_btn":
        if button.width() != mw.window().width()*0.3:
            update_streak_btn()

    if message in ["ease1", "ease2", "ease3", "ease4"]:
        add_msg_to_db(message)
    return handled


def start_game():
    try:
        streakgame.main.main()
    except pygame.error as e:
        print(e)


def start_rpg():
    mw.win = win = QMainWindow()
    rpg_popup(win)


def on_profile_open():
    pygame.init()
    info = pygame.display.Info()    
    mw.window().setGeometry(10,60,info.current_w,info.current_h-70)
    center_widget(mw.window())
    global button
    button = QPushButton(mw)
    cwd = os.getcwd()+os.sep[0]
    addon_name = mw.addonManager.addonFromModule(__name__)
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)),addon_name ,f"assets/ui/sunset.gif").replace(cwd, '').replace(os.sep[0],'/')
    button.setStyleSheet(f'''border-image : url({path});
                
                height: 100%;
                width: 100%;                             
                background-position: center;
                background-repeat: no-repeat;                           ''')
    update_streak_btn()    
    button.show()
    button.clicked.connect(start_game)
    due_tree = mw.col.sched.deck_due_tree()
    to_review = due_tree.review_count + due_tree.learn_count + due_tree.new_count
    data = json.load(open(anki_data_path, 'r'))
    data['nb_cards_to_review_today'] = to_review
    json.dump(data, open(anki_data_path, "w"))


def update_streak_btn():
    global button
    size = mw.window().geometry()
    print(size)
    if not button: return
    size = [size.width(),size.height()]
    if size[1] < 630 or size[0] < 750:
        button.hide()
    else:
        button.show()  
    button.setGeometry(size[0]*0.35, size[1]*0.6, size[0]*0.3, size[1]*0.3)


# Inject a button in the deck view
def update_streak_btn_js(
    web_content: WebContent, context: object | None
) -> None:
    if not isinstance(context, DeckBrowser):
        return
    web_content.body += f"""
<script>
setInterval(() => {{
pycmd("update_streak_btn");
}}, 100);    
</script>
    """


gui_hooks.profile_did_open.append(on_profile_open)
gui_hooks.reviewer_did_answer_card.append(process_file)
aqt.gui_hooks.overview_will_render_content.append(add_btn)
aqt.gui_hooks.overview_will_render_content.append(lambda x,y: button.hide())
aqt.gui_hooks.webview_did_receive_js_message.append(bridge)
gui_hooks.webview_will_set_content.append(update_streak_btn_js)
