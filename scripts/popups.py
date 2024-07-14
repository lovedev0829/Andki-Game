from scripts.utils import center_widget, get_data, change_data
from aqt.qt import *
from aqt import mw
from functools import partial
import random
from scripts.constants import *
class rpg_popup:
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
class trainer_challenge:
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

class trainer_popup:
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
Ankimons = ["AnkiNick","Beekeeper Alder King","Primus Nephritico","Silver Globe Knight","Chrome-coated info soap","Immune Shield Globe Knight","Icy Gold Pastor","Illuminated goblin","Ancient evergreen reactor","Tent landlord Hedgehog Moon","Plump Bell Ogre","Clever Maasai Gold Net Warrior","Diamond Ninja Messenger","Glowing Net Knight"]
def load_sheet(i):
	cwd = os.getcwd()+os.sep[0]
	path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets//heads//{Ankimons[i]}.png").replace(cwd, '').replace(os.sep[0],'/')
	print(path)
	return	f'''border-image : url({path});
				
				height: 100%;
				width: 100%;                             
				background-position: center;
				background-repeat: no-repeat;                           '''

class attribute_popup:
	def __init__(self, win):
		self.counter = 0
		# set the title
		self.things = []
		self.selected = [None for i in range(3)]
		win.setWindowTitle("Anki Habitica")        
		# setting the geometry of window
		win.setFixedSize(700,400)
		center_widget(win)
		data = get_data()
		self.Ankimons = ["AnkiNick","Beekeeper Alder King","Primus Nephritico","Silver Globe Knight","Chrome-coated info soap","Immune Shield Globe Knight","Icy Gold Pastor","Illuminated goblin","Ancient evergreen reactor","Tent landlord Hedgehog Moon","Plump Bell Ogre","Clever Maasai Gold Net Warrior","Diamond Ninja Messenger","Glowing Net Knight"]

		self.tempwin = None
		self.buttons : list[QPushButton] = []
	
		for i in range(3):
			self.buttons.append(QPushButton(win))
			
			self.buttons[i].animateClick()
			self.buttons[i].setGeometry(70+i*200,90,150,150)
			
			self.buttons[i].setStyleSheet(f'''border-image : url(assets/ui/empty.PNG);
			
			height: 100%;
			width: 100%;                             
			background-position: center;
			background-repeat: no-repeat;                           ''')
			self.buttons[i].clicked.connect(partial(self.clicked,i))
		if data['default_ankimon']:
			self.selected = data['default_ankimon']
			self.update_ui()
		# show all the widgets

		win.show()

	def clicked(self, index):
		self.counter += 1
		if self.counter > 3:	
			self.tempwin = QMainWindow()		
			self.things.append(ankimon_selector(self.tempwin, self, index))

	def update_ui(self):
		
		for i, button in enumerate(self.buttons):
			try:
				button.setStyleSheet(load_sheet(self.Ankimons.index(self.selected[i])))
				QPixmap(f"assets/heads/{self.selected[i]}.png")
				change_data("default_ankimon", self.selected)
			except TypeError as e:
				print(e)

class ankimon_selector:
	def __init__(self, win:QMainWindow, attribute: attribute_popup, index):
		self.ankimon_index = index
		# set the title
		self.attribute = attribute
		self.win = win
		win.setWindowTitle("Anki Habitica")        
		# setting the geometry of window
		win.setFixedSize(840,580)
		center_widget(win)
		central_widget = win
		data = get_data()
		self.Ankimons = attribute.Ankimons
		self.buttons : list[QPushButton] = []
		labels : list[QLabel] = []
        # Create a scroll area
		scroll_area = QScrollArea(win)
		scroll_area.setWidgetResizable(True)

		# Adjust scroll bar value to move elements
		bar = scroll_area.verticalScrollBar()
		bar.valueChanged.connect(self.on_scroll)		
		bar.move(20,20)
		self.counter = 0
		index = 0
		for i in range(len(self.Ankimons)):
			if self.Ankimons[i] not in self.attribute.selected:
				self.buttons.append(QPushButton(central_widget))
				labels.append(QLabel(parent=central_widget,text=str(index)))
				labels[index].adjustSize()
				labels[index].setGeometry(110+(index%4)*200,110+180*(index//4),150,150)
				self.buttons[index].animateClick()
				self.buttons[index].setGeometry(40+(index%4)*200,20+180*(index//4),150,150)
				
				print(os.getcwd())
				self.buttons[index].setStyleSheet(load_sheet(i))
				self.buttons[index].clicked.connect(partial(self.clicked,i))
				index += 1

		# show all the widgets
		self.completed = False
		win.show()
		if self.completed:
			return

	def clicked(self, i):
		if self.counter > len(self.buttons)-1:
			try:
				self.attribute.selected[self.ankimon_index] = self.Ankimons[i]
			except IndexError as e:
				print(e)
				self.attribute.selected.append(self.Ankimons[i])
			self.completed = True
			self.attribute.tempwin = None
			self.win = None
			self.attribute.update_ui()
		self.counter += 1
	def on_scroll(self, value):
		for element in self.win.children():
			element.move(element.x(), element.y()-value)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    choose_option = QMainWindow()
    ui = rpg_popup()
    ui.setupUi(choose_option)
    choose_option.show()
    sys.exit(app.exec_())