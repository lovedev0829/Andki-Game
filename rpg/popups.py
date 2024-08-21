import sys
from aqt.qt import *
import aqt.utils
import pygame
import aqt
from aqt import mw
import random
from functools import partial
from scripts.utils import get_data, change_data, anki_data_path, xp_to_lvl
from scripts.constants import *
from scripts.constants import trainer_xp
from scripts.popups import center_widget
import json
from enum import Enum

class Rewards(Enum):
    RELEASE = 150

def load_sheet(i, folder='heads', names:list[str]=None):
	cwd = os.getcwd()+os.sep[0]
	path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",folder,f"{names[i]}.png"if 'png' not in names[i].lower() else names[i]).replace(cwd, '').replace(os.sep[0],'/')
	print(path)
	return	f'''border-image : url({path});
				
				height: 100%;
				width: 100%;                             
				background-position: center;
				background-REPEAT: no-repeat;                           '''

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
        self.label = QLabel("Would you like to save your game?")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(self.label)
        
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
            print('wildankimon close event ran with successful condition')
            self.game.ankiwin = captured_ankimon(self.name, self.coords, self.game)
        else:
            print('wildankimon close event ran with failed condition')
            self.game.ankiwin = None
        event.accept()


class captured_ankimon(QMainWindow):
    def __init__(self, name, coords, game):
        super().__init__()
        self.setWindowTitle("Ankimon")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(640,480)
        self.action = None
        self.required_cards = 1000
        self.coords = coords
        self.completed_cards = 0
        self.action = None
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
            self.text_label.move(75,15)
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
        mob = self.game.engine.get_mob(*self.coords[1])
        mob.health = min(mob.maxhealth, mob.health + mob.maxhealth*0.1)
        aqt.utils.showInfo("You're attacked Ankimon has been healed 10%")
        self.close()

    def capturefunc(self):
        UNLOCKED_ANKIMONS.append(self.name)  
        change_data('Unlocked_Ankimons', UNLOCKED_ANKIMONS)
        self.close()

    def closeEvent(self, event):
        self.game.ankiwin = None

        event.accept()
        
        

class trainer_xp_window(QMainWindow):
    def __init__(self, game):
        super().__init__()
        self.counter = 0
        self.setWindowTitle("AnkiNick-mon")        
        self.game = game
        self.ratio = .6
        self.setFixedSize(700,400)
        center_widget(self)
        data = get_data()
        self.trainers = TRAINERS
        self.buttons : list[QPushButton] = []
        self.item = data.get('item', None)
        self.level = xp_to_lvl(data.get('trainer_xp', 0))
        self.set_ratio(self.level%1)
        self.label = QLabel(self)
        self.label.setText(f"""you have gained {(get_data().get('trainer_xp',0)-self.game.trainer_xp)*2}xp for your trainer
                           lvl{int(self.level)}""")
        self.label.setFont(QFont(self.label.font().toString(),15))
        self.label.adjustSize()
        self.label.move(self.width()/2-self.label.width()/2,5)
        for i in range(1):
            self.buttons.append(QPushButton(self))
            self.buttons[i].animateClick()
            self.buttons[i].setGeometry(260+i*220,90+i*50,150-i*100,180-i*100+int(not i)*30)
            self.buttons[i].setStyleSheet(load_sheet(self.trainers.index(get_data().get('default_trainer')), 'trainers', self.trainers))
        if data.get('default_trainer', None):
            self.selected = [data['default_trainer']]
            self.update_ui()
        # show all the widgets
        self.okbutton = QPushButton(self,text="OK")
        self.okbutton.setGeometry(QRect(265, 320, 141, 51))
        self.okbutton.clicked.connect(self.close)
        

        self.show()
        

    def set_ratio(self, ratio):
        """Sets the health ratio and updates the display."""
        self.ratio = max(0, min(1, ratio))  # Ensure ratio is between 0 and 1
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get current window size
        current_width = self.width()//4
        current_height = 20
        # Draw a border around the health bar
        painter.setPen(QColor(0, 0, 0))
        painter.drawRect(current_width*1.42, 60, current_width-1, current_height-1)
        # Draw foreground (filled part of the health bar based on ratio)
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        filled_width = current_width * self.ratio
        painter.drawRect(current_width*1.42, 60, filled_width, current_height)

    def update_ui(self):
        for i, button in enumerate(self.buttons):
            try:
                if i == 1:
                    if self.item:
                        button.setStyleSheet(load_sheet(ITEMS.index(self.item), 'items', ITEMS))
                        change_data("item", self.item)				
                else:
                    button.setStyleSheet(load_sheet(self.trainers.index(self.selected[i]), 'trainers', self.trainers))
                    change_data("default_trainer", self.selected[0])
            except Exception as e:
                print(e)
                

    def close(self, event):
        pygame.quit()
        self.game.ankiwin = None
        mw.window().showMaximized()
        print(event)

        del self.game
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
    def __init__(self, game, won=True):
        super().__init__()
        
        # set the title
        self.setWindowTitle("AnkiNick-mon")
        # setting the geometry of window
        self.setFixedSize(640,480)
        center_widget(self)
        trainer_xp = get_data().get('trainer_xp',0)
        if won:
            possible_winnings = [anki for anki in ANKIMONS if anki not in UNLOCKED_ANKIMONS]
            print(possible_winnings)
            xp = trainer_xp - game.trainer_xp
            trainer_xp += xp

            change_data('trainer_xp', trainer_xp)
            image_name = None
            if possible_winnings:
                image_name = random.choice(possible_winnings)
                self.text_label = QLabel(f"congratulations on winning you unlocked a new Ankimon \n {image_name}" if image_name else '', self)
                UNLOCKED_ANKIMONS.append(image_name)
                change_data('Unlocked_Ankimons', UNLOCKED_ANKIMONS)
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
                self.text_label.adjustSize()
                self.text_label.move(80,15)
            else:
                self.text_label = QLabel(f"congratulations on winning", self)
                self.text_label.adjustSize()
                self.text_label.move(190,15)

            
        else:
            self.text_label = QLabel(f"You have lost better luck next time!", self)
            self.text_label.move(165,10)                        
        print(won)
        self.okbutton = QPushButton(parent=self,text="OK")
        self.okbutton.move(self.width()/2-self.okbutton.width()/2,440)
        self.okbutton.clicked.connect(self.close)
        self.okbutton.keyPressEvent = self.keyPressEvent

        self.game = game
        self.text_label.setFont(QFont(self.text_label.font().toString(),15))
        self.text_label.adjustSize()
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        # show all the widgets
        self.show()

    def close(self, event):
        self.game.ankiwin = trainer_xp_window(self.game)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            event.ignore()  # Ignore the space bar press
        else:
            super().keyPressEvent(event)
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
