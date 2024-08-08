from __future__ import annotations
import datetime
import json
import os.path
import sys
sys.path.append(os.path.dirname(__file__))
import threading
import base64
import aqt.utils
import pygame
from aqt import gui_hooks, mw
from aqt.qt import * 
import streakgame.main
from rpg.main import mainloop
from scripts.utils import process_file, add_msg_to_db, add_btn, center_widget, get_html, image_to_base64, manager
import asyncio, time
from scripts.popups import rpg_popup, attribute_popup, LoginHandler
from aqt.deckbrowser import DeckBrowser
from aqt.webview import WebContent


#global vars
cwd = os.path.dirname(__file__)

anki_data_path = os.path.join(cwd, "anki_data.json")
size = [300,300]

started = False
stats = manager()

def bridge(handled, message: str, context):
    global started
    
    for message in message.split(' '):
        print(message)
        if message == "start_rpg":
            start_rpg()
        if message == "start_streak":
            start_game()
        if message == "attribute":
            mw.win = QMainWindow()
            from scripts import utils
            attribute_popup(mw.win, True if utils.started else False)

        if message in ["ease1", "ease2", "ease3", "ease4"]:
            add_msg_to_db(message)
    return handled


def start_game():
    mw.win = win = QMainWindow() 
    LoginHandler(win)


def start_rpg():
    mw.win = win = QMainWindow()
    rpg_popup(win)

screen_size = []
def on_profile_open():
    pygame.init()
    info = pygame.display.Info()    
    global screen_size
    screen_size = [info.current_w, info.current_h]
    mw.window().setGeometry(10,60,info.current_w,info.current_h-70)
    center_widget(mw.window())
    due_tree = mw.col.sched.deck_due_tree()
    to_review = due_tree.review_count + due_tree.learn_count + due_tree.new_count
    data = json.load(open(anki_data_path, 'r'))
    data['nb_cards_to_review_today'] = to_review
    json.dump(data, open(anki_data_path, "w"))



cwd = os.path.dirname(__file__)
path = os.path.join(cwd, f"assets","image.png"    )
# Inject a button in the deck view
def update_streak_btn_js(
    web_content: WebContent, context: object | None
) -> None:
    if not isinstance(context, DeckBrowser):
        return
    addon_name = mw.addonManager.addonFromModule(__name__)
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, "assets", "ui","Farm.gif")
    print(path)
    base64_image = image_to_base64(path)
    web_content.body += get_html(base64_image, "start_streak")
mw.addonManager.setWebExports(__name__, path)


gui_hooks.profile_did_open.append(on_profile_open)
gui_hooks.reviewer_did_answer_card.append(process_file)
aqt.gui_hooks.overview_will_render_content.append(add_btn)
aqt.gui_hooks.webview_did_receive_js_message.append(bridge)
gui_hooks.webview_will_set_content.append(update_streak_btn_js)
