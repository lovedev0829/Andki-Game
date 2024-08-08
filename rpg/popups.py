import sys
from aqt.qt import *
import pygame
from aqt import mw
import random
from scripts.constants import ANKIMONS, TRAINERS, anki_data_path as data_path
from scripts.popups import center_widget
import json

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

class trainer_popup(QMainWindow):
    def __init__(self, cost):
        super().__init__()
        
        # set the title
        self.setWindowTitle("AnkiNick-mon")
        self.cost = cost
        # setting the geometry of window
        self.setFixedSize(500,180)
        center_widget(self)

        # creating label
        self.label = QLabel(self)
        self.text_label = QLabel(f"""So you want to take on the next challenge?
    I'll show you that I'm the best 
    AnkiMon trainer here, not you!
    learn 10 cards to accept the challenge
    0/{self.cost}
                            """, self)
        self.text_label.setFont(QFont(self.text_label.font().toString(),15))
        self.text_label.adjustSize()
        self.text_label.move(10,15)
        # loading image
        scaler = 2
        
        image_name = random.choice(TRAINERS)
        self.pixmap = QPixmap(image_name)
        # self.pixmap.	
        # adding image to label
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
        # self.okbutton = QPushButton(self)
        # self.okbutton.setGeometry(QRect(180, 170, 91, 51))
        # self.okbutton.setObjectName("okbutton")
        # self.okbutton.clicked.connect(lambda : self.close())
        # self.okbutton.setText("OK")
        
        # show all the widgets
        self.show()
        
    def closeEvent(self, event:QCloseEvent):
        if int((self.cards - learned_card_checker(data_path))*10) >= self.cost:
            print('Congratulations! You accepted the challenge!')
            event.accept()
        else:
            event.ignore()

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
