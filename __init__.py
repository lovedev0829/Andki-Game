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

cwd = os.path.dirname(__file__)

anki_data_path = os.path.join(cwd, "anki_data.json")
size = [300,300]


started = False
stats = manager()

def bridge(handled, message: str, context):
    global started
    if message == "start_rpg":
        if not started:
            start_rpg()
            started = True
    if message == "attribute":
        mw.win = QMainWindow()
        attribute_popup(mw.win)
    if message == 'rerender':
        pass
    if message in ["ease1", "ease2", "ease3", "ease4"]:
        add_msg_to_db(message)
    return handled


aqt.gui_hooks.overview_will_render_content.append(add_btn)
aqt.gui_hooks.webview_did_receive_js_message.append(bridge)
# aqt.gui_hooks.
# Add a button to the main screen with title "start game" and that starts the game when clicked

def start_game():
    global pygame_instace
    pygame_instace = streakgame.main.mainnowin(stats)
    

def start_rpg():
    global pygame_instace
    mw.win = win = QMainWindow()
    rpg_popup(win)
    

def on_profile_open():
    due_tree = mw.col.sched.deck_due_tree()
    to_review = due_tree.review_count + due_tree.learn_count + due_tree.new_count
    if to_review:
        aqt.utils.show_info(f"You have {to_review} cards to learn today. Good luck !")
    
    data = json.load(open(anki_data_path, 'r'))
    data['nb_cards_to_review_today'] = to_review
    json.dump(data, open(anki_data_path, "w"))
    # center_widget(mw.menuWidget())
    try:
        start_game()
    except pygame.error as e:
        print(e)

gui_hooks.profile_did_open.append(on_profile_open)
gui_hooks.reviewer_did_answer_card.append(process_file)


def on_webview_will_set_content(
    web_content: WebContent, context: object | None
) -> None:
    if not isinstance(context, DeckBrowser):
        return
    addon_name = mw.addonManager.addonFromModule(__name__)
    pos = mw.app.primaryScreen().size().width()/2 - stats.SIZE[0]/2
    buf = 5
    # path = f"/_addons/{addon_name}/assets/temp/{main.Frame}.png"
    css = f"""    <style>
        .img {{
            position: relative;
            left: {pos}px;
        }}
    </style>        """
    web_content.body += (
        f'''
{css}
<div >
<img class="img" src="image.png" margin id="anki";">
</div>
<script>
let img = document.getElementById("anki");
let counter = 0;
setInterval(() => {{
    document.getElementById("anki").src = '/_addons/{addon_name}/assets/temp/'+Math.floor(counter/{buf})*{buf}+'.png'; 
    document.getElementById("anki").onerror = function(){{
        counter -= 2.7;
        for (let i =0; i > 8; i=i){{
            document.getElementById("anki").src = '/_addons/{addon_name}/assets/temp/'+Math.floor((counter-{buf*stats.buffer_size}/i)/{buf})*{buf}+'.png'; 
            document.getElementById("anki").onerror = function(){{
                i++;
            }}
        }}
        
    }}
    counter += 0.89;
    counter = Math.max(counter, {stats.Frame-buf*stats.buffer_size/2}+60)
}}, 1100/60);
</script>''')

gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
mw.addonManager.setWebExports(__name__, r"assets/.*.png")
mw.addonManager.setWebExports(__name__, r"assets/temp/.*.png")