import sys
from aqt.qt import *
import aqt.utils
import pygame
import aqt
from aqt import mw
import random
from functools import partial
from scripts.utils import get_data, change_data, anki_data_path
from scripts.constants import *
from scripts.constants import trainer_xp
from scripts.popups import center_widget
import json
from enum import Enum

class Rewards(Enum):
    RELEASE = 150


def learned_card_checker(data_path):
    with open(data_path, "r") as f:
        data = json.load(f)
    if 'moves' not in data:
        learned_cards = data['nb_cards_learned_today']
        data['moves'] = learned_cards
        json.dump(data, open(data_path, 'w'))
    else:
        learned_cards = data['moves']
    return learned_cards
class SaveWindow(QMainWindow):
    def __init__(self, func, game):
        super().__init__()
        self.setWindowTitle("Save Window")
        self.move(100, 100)
        self.setFixedSize(400, 200)
        
        center_win(self)
        self.game = game
        self.save_func = func        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_widget.setLayout(main_layout)
        
        # Label
        label = QLabel("Would you like to save your game?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(label)
        
        # Button layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        main_layout.addLayout(button_layout)
        
        # OK button
        ok_button = QPushButton("OK")
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        ok_button.clicked.connect(self.save_file)
        button_layout.addWidget(ok_button)
        
        # No button
        no_button = QPushButton("No")
        no_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; 
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        no_button.clicked.connect(self.close_window)
        button_layout.addWidget(no_button)
        self.show()        
    def save_file(self):
        self.save_func()
        self.close_window()
    def close_window(self):
        self.close()
        pygame.quit()
        pygame.init()
        info = pygame.display.Info()
        self.game.ankiwin = None
        mw.window().setGeometry(10,60,info.current_w,info.current_h-70)
        center_widget(mw.window())
        pygame.quit()

class ActionWindow(QMainWindow):
    def __init__(self, action, required_cards, coords, game):
        super().__init__()
        self.setWindowTitle("Ankimon")
        self.setGeometry(100, 100, 400, 200)
        self.completed_cards = 0
        self.action = action
        self.required_cards = required_cards
        self.coords = coords
        self.game = game
        center_win(self)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_widget.setLayout(main_layout)
        
        # Label
        self.label = QLabel(f"""You want to {self.action.value}, give me {self.required_cards} cards!!!
                       
                       
{self.completed_cards}/{self.required_cards}""")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(self.label)
        self.show()        

    def closeEvent(self, event):
        self.game.ankiwin = None
        event.accept()

    def save_file(self):
        self.save_func()
        self.close_window()
    def close_window(self):
        self.close()
        pygame.quit()
        pygame.init()
        info = pygame.display.Info()
        
        mw.window().setGeometry(10,60,info.current_w,info.current_h-70)
        center_widget(mw.window())
        pygame.quit()

class WildAnkimon(QMainWindow):
    def __init__(self, required_cards, coords, game):
        super().__init__()
        self.setWindowTitle("Ankimon")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(640,480)
        self.coords = coords
        self.ratio = 1
        self.action = None
        self.required_cards = required_cards
        self.completed_cards = 0
        self.game = game
        center_win(self)
        
        global trainer_xp

        image_name = random.choice(ANKIMONS)
        self.text_label = QLabel(f"""   A wild ankimon has approached you, learn {self.required_cards} cards to capture it
    {self.completed_cards}/{self.required_cards}""",self)
        self.text_label.move(25,15)
        cwd = os.getcwd()+os.sep[0]        
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",'heads',f"{image_name}.png").replace(cwd, '').replace(os.sep[0],'/')
        self.name = image_name
        self.label = QLabel(self)
        self.pixmap = QPixmap(path)        
        self.label.setPixmap(self.pixmap)
        scaler = 0.6
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width()*scaler,
                        self.pixmap.height()*scaler)
        self.label.setScaledContents(True)
        self.label.move(100,50)
        self.text_label.setFont(QFont(self.text_label.font().toString(),15))
        self.text_label.adjustSize()
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # show all the widgets
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        try:
            self.ratio = self.completed_cards/self.required_cards
        except ZeroDivisionError:
            self.ratio = 1
        # Get current window size
        current_width = self.width()//2
        current_height = 25
        # Draw a border around the health bar
        painter.setPen(QColor(0, 0, 0))
        painter.drawRect(current_width/2, 105, current_width-1, current_height-1)
        # Draw foreground (filled part of the health bar based on ratio)
        painter.setBrush(QBrush(Qt.GlobalColor.red))
        painter.drawRect(current_width/2, 105, current_width, current_height)
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        filled_width = current_width * (1-self.ratio)
        painter.drawRect(current_width/2, 105, filled_width, current_height)

    def closeEvent(self, event):
        if self.completed_cards >= self.required_cards:
            self.game.ankiwin = captured_ankimon(self.name, self.coords, self.game)
        else:
            self.game.ankiwin = None
        event.accept()


class captured_ankimon(QMainWindow):
    def __init__(self, name, coords, game):
        super().__init__()
        self.setWindowTitle("Ankimon")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(640,480)
        self.action = None
        self.required_cards = 10
        self.coords = coords
        self.completed_cards = 0
        self.game = game
        center_win(self)
        
        global trainer_xp
        # self.text_label.move(25,15)
        cwd = os.getcwd()+os.sep[0]       
        self.name = name 
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",'heads',f"{name}.png").replace(cwd, '').replace(os.sep[0],'/')
        self.label = QLabel(self)
        self.pixmap = QPixmap(path)        
        # OK button
        

        self.label.setPixmap(self.pixmap)
        scaler = 0.6
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width()*scaler,
                        self.pixmap.height()*scaler)
        self.label.setScaledContents(True)
        self.label.move(100,30)

        if name in UNLOCKED_ANKIMONS:
            self.text_label = QLabel(f"""you have defeated the ankimon would you like to release it for xp """,self)
            self.text_label.move(25,15)
            self.ok_button = QPushButton(text="OK", parent=self)
            self.ok_button.move(280,420)
            self.ok_button.clicked.connect(self.releasefunc)
            self.ok_button.setEnabled(True)
        else:
            self.text_label = QLabel(f"""you have defeated the ankimon would you like to capture it 
            or release it for xp""",self)
            self.text_label.move(45,15)
            self.capture = QPushButton(text="capture", parent=self)
            self.capture.move(170,420)
            self.capture.clicked.connect(self.capturefunc)
            self.capture.setEnabled(True)

            self.release = QPushButton(text="release", parent=self)
            
            self.release.clicked.connect(self.releasefunc)
            self.release.move(400,420)
            self.release.setEnabled(True)          
        self.text_label.setFont(QFont(self.text_label.font().toString(),15))
        self.text_label.adjustSize()
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # show all the widgets
        self.show()

    def releasefunc(self):
        xp = get_data().get('trainer_xp', 0)
        change_data('trainer_xp', xp+Rewards.RELEASE.value)  
        self.close()

    def capturefunc(self):
        UNLOCKED_ANKIMONS.append(self.name)  
        change_data('Unlocked_Ankimons', UNLOCKED_ANKIMONS)
        self.close()

    def closeEvent(self, event):
        self.game.ankiwin = None
        mob = self.game.engine.get_mob(*self.coords[1])
        mob.health = mob.maxhealth
        event.accept()
        aqt.utils.showInfo("You're attacked Ankimon has been fully healed")
        




class trainer_popup(QMainWindow):
    def __init__(self, cost, image_name):
        super().__init__()
        
        # set the title
        self.setWindowTitle("AnkiNick-mon")
        self.cost = cost
        self.required_cards = cost
        self.completed_cards = 0
        # setting the geometry of window
        self.setFixedSize(500,180)
        center_widget(self)

        # creating label
        self.label = QLabel(self)
        print(cost)
        self.text_label = QLabel(f"", self)
        self.text_label.setFont(QFont(self.text_label.font().toString(),15))
        self.text_label.adjustSize()
        self.text_label.move(10,15)
        # loading image
        scaler = 2
        
 
        cwd = os.getcwd()+os.sep[0]        
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",'trainers',f"{image_name}.png").replace(cwd, '').replace(os.sep[0],'/')
        
        self.pixmap = QPixmap(path)        
        self.label.setPixmap(self.pixmap)

        # Optional, resize label to image size
        self.label.resize(self.pixmap.width()*scaler,
                        self.pixmap.height()*scaler)
        self.label.setScaledContents(True)
        self.label.move(380,20)
        if image_name.startswith('Scientist'):		
            # Flip the QPixmap horizontally if the name of trainer starts with scientist
            transform = QTransform().scale(-1, 1)
            flipped_pixmap = self.pixmap.transformed(transform)
            # Set the flipped QPixmap to the QLabel
            self.label.setPixmap(flipped_pixmap)              
        
        # show all the widgets
        self.show()
        
    def closeEvent(self, event:QCloseEvent):
        if int((self.cards - learned_card_checker(anki_data_path))*10) >= self.cost:
            print('Congratulations! You accepted the challenge!')
            event.accept()
        else:
            event.ignore()


class Win_popup(QMainWindow):
    def __init__(self, xp=10, won=True):
        super().__init__()
        
        # set the title
        self.setWindowTitle("AnkiNick-mon")
        # setting the geometry of window
        self.setFixedSize(640,480)
        center_widget(self)

        global trainer_xp
        if won:
            possible_winnings = [anki for anki in ANKIMONS if anki not in UNLOCKED_ANKIMONS]
            trainer_xp += xp

            change_data('trainer_xp', trainer_xp)
            image_name = None
            if possible_winnings:
                image_name = random.choice(possible_winnings)
                UNLOCKED_ANKIMONS.append(image_name)
                change_data('Unlocked_Ankimons', UNLOCKED_ANKIMONS)

            self.text_label = QLabel(f"congratulations on winning you have won {xp}xp"+f' and a new Ankimon \n {image_name}' if image_name else '', self)
            self.text_label.move(25,15)
            cwd = os.getcwd()+os.sep[0]        
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",'heads',f"{image_name}.png").replace(cwd, '').replace(os.sep[0],'/')
            print(path)
            self.label = QLabel(self)
            self.pixmap = QPixmap(path)        
            self.label.setPixmap(self.pixmap)
            scaler = 0.6
            # Optional, resize label to image size
            self.label.resize(self.pixmap.width()*scaler,
                            self.pixmap.height()*scaler)
            self.label.setScaledContents(True)
            self.label.move(100,30)
        else:
            self.text_label = QLabel(f"You have lost better luck next time!", self)
            self.text_label.move(160,10)                        
        self.text_label.setFont(QFont(self.text_label.font().toString(),15))
        self.text_label.adjustSize()
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # show all the widgets
        self.show()


def center_win(win:QMainWindow):
    pygame.init()
    info = pygame.display.Info()
    size = info.current_w,info.current_h
    win.move(info.current_w*(3/2) -win.geometry().width()/2, info.current_h/2 - win.geometry().height()/2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SaveWindow('s')
    win.show()
    sys.exit(app.exec())
