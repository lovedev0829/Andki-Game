from __future__ import annotations
import datetime
import json
import sys
import os
import aqt.qt
sys.path.append(os.path.dirname(__file__))
import aqt.utils
from aqt import gui_hooks, mw
from aqt.qt import * 
import streakgame.main
from rpg.main import mainloop
from scripts.utils import change_data, process_file, add_msg_to_db, add_btn, center_widget, get_html, image_to_base64, xp_to_lvl, get_data, manager
from scripts.popups import rpg_popup, attribute_popup, LoginHandler, DifficultyChoosingWindow, TrainerCustomizationWindow
from aqt.deckbrowser import DeckBrowser
from aqt.webview import WebContent
def change_difficulty():
    mw.win = DifficultyChoosingWindow()

def menusetup()-> QMenu:
    menu = QMenu("AnkiNick", mw)
    menu.addAction("Change Difficulty").triggered.connect(change_difficulty)
    menu.addAction("Customize Trainer").triggered.connect(lambda: TrainerCustomizationWindow())
    mw.form.menubar.addMenu(menu)
    return menu
