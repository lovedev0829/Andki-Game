import sys
from aqt.qt import *
import pygame
from aqt import mw
from scripts.popups import center_widget
class SaveWindow(QMainWindow):
    def __init__(self, func):
        super().__init__()
        self.setWindowTitle("Save Window")
        self.setGeometry(100, 100, 400, 200)
        center_win(self)
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
        print(info)
        mw.window().setGeometry(10,60,info.current_w,info.current_h-70)
        center_widget(mw.window())
        pygame.quit()

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
