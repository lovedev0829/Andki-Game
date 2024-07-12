from scripts.utils import center_widget, get_data
from aqt.qt import *
from aqt import mw
from functools import partial
import random
from scripts.constants import *
class rpg_popup():
    def setupUi(self, choose_option):
        choose_option.setObjectName("choose_option")
        choose_option.resize(598, 347)
        self.pushButton = QPushButton(choose_option)
        self.pushButton.setGeometry(QRect(90, 100, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(choose_option)
        self.pushButton_2.setGeometry(QRect(350, 100, 161, 51))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setBaseSize(QSize(0, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.okbutton = QPushButton(choose_option)
        self.okbutton.setGeometry(QRect(210, 240, 191, 51))
        self.okbutton.setSizeIncrement(QSize(0, 0))
        self.okbutton.setBaseSize(QSize(0, 0))
        self.okbutton.setObjectName("okbutton")
        self.okbutton.clicked.connect(delete_win)
        
        self.menubar = QMenuBar(choose_option)
        self.menubar.setGeometry(QRect(0, 0, 598, 21))
        self.menubar.setObjectName("menubar")
        choose_option.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(choose_option)
        self.statusbar.setObjectName("statusbar")
        choose_option.setStatusBar(self.statusbar)

        self.retranslateUi(choose_option)
        QMetaObject.connectSlotsByName(choose_option)

    def retranslateUi(self, choose_option):
        _translate = QCoreApplication.translate
        choose_option.setWindowTitle(_translate("choose_option", "Anki Habitica"))
        self.pushButton.setText(_translate("choose_option", "solo Adventure"))
        self.pushButton_2.setText(_translate("choose_option", "challenge a friend"))
        self.okbutton.setText(_translate("choose_option", "ok"))
class trainer_challenge():
    def setupUi(self, choose_option):
        choose_option.setObjectName("choose_option")
        screen_size = mw.app.primaryScreen().size()
        screen_size = [screen_size.width(), screen_size.height()]
        window_size = 600, 350
        self.setGeometry(screen_size[0]//2-window_size[0]//2, screen_size[1]//2-window_size[1]//2, *window_size)
        self.setFixedSize(*window_size)
        self.pushButton = QPushButton(choose_option)
        self.pushButton.setGeometry(QRect(90, 100, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(choose_option)
        self.pushButton_2.setGeometry(QRect(350, 100, 161, 51))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setBaseSize(QSize(0, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.okbutton = QPushButton(choose_option)
        self.okbutton.setGeometry(QRect(210, 240, 191, 51))
        self.okbutton.setSizeIncrement(QSize(0, 0))
        self.okbutton.setBaseSize(QSize(0, 0))
        self.okbutton.setObjectName("okbutton")
        self.okbutton.clicked.connect(delete_win)
        
        self.menubar = QMenuBar(choose_option)
        self.menubar.setGeometry(QRect(0, 0, 598, 21))
        self.menubar.setObjectName("menubar")
        choose_option.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(choose_option)
        self.statusbar.setObjectName("statusbar")
        choose_option.setStatusBar(self.statusbar)

        self.retranslateUi(choose_option)
        QMetaObject.connectSlotsByName(choose_option)

    def retranslateUi(self, choose_option):
        _translate = QCoreApplication.translate
        choose_option.setWindowTitle(_translate("choose_option", "Anki Habitica"))
        self.pushButton.setText(_translate("choose_option", "solo Adventure"))
        self.pushButton_2.setText(_translate("choose_option", "challenge a friend"))
        self.okbutton.setText(_translate("choose_option", "ok"))


def delete_win():
    mw.win = None

class trainer_popup():
	def __init__(self, win):
		
        
		# set the title
		win.setWindowTitle("Anki Habitica")
        
		# setting the geometry of window
		win.setFixedSize(500,200)
		center_widget(win)

		# creating label
		self.label = QLabel(win)
		self.text_label = QLabel("""So you want to take on the next challenge?
I'll show you that I'm the best 
AnkiMon trainer here, not you!""", win)
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
		self.okbutton = QPushButton(win)
		self.okbutton.setGeometry(QRect(180, 140, 91, 51))
		self.okbutton.setObjectName("okbutton")
		self.okbutton.clicked.connect(delete_win)
		self.okbutton.setText("OK")
        
		# show all the widgets
		win.show()

class attribute_popup():
	def __init__(self, win):
		# set the title
		win.setWindowTitle("Anki Habitica")        
		# setting the geometry of window
		win.setFixedSize(700,400)
		center_widget(win)
		data = get_data()
        
		buttons : list[QPushButton] = []
		if not data['default_ankimon']:
			for i in range(3):
				buttons.append(QPushButton(win))
				
				buttons[i].animateClick()
				buttons[i].setGeometry(40+i*220,70,180,200)
				
				buttons[i].setStyleSheet(f'''background-image : url(assets/ui/empty.PNG);
				
				height: 100%;
				width: 100%;                             
				background-position: center;
				background-repeat: no-repeat;                           ''')
				buttons[i].clicked.connect(partial(self.clicked,i))
		# show all the widgets
		win.show()
	

	def clicked(self, index):
            print(index)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    choose_option = QMainWindow()
    ui = rpg_popup()
    ui.setupUi(choose_option)
    choose_option.show()
    sys.exit(app.exec_())
