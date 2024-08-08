from scripts.utils import center_widget, get_data, change_data
from aqt.qt import *

import threading
from aqt import mw
from aqt import utils
from rpg.main import mainloop
from functools import partial
import json
from rpg.ankirpg import data_path
import random
from scripts.constants import cwd, ANKIMONS, TRAINERS


def delete_win():
    mw.win = None

def start_chess(ankimons:dict, load_save=False):
	delete_win()
	mw.web.eval("pycmd('study');")
	mainloop(ankimons, load_save)
started = False

Ankimons = ANKIMONS
def load_sheet(i, folder='heads', names=Ankimons):
	cwd = os.getcwd()+os.sep[0]
	path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",folder,f"{names[i]}.png").replace(cwd, '').replace(os.sep[0],'/')
	print(path)
	return	f'''border-image : url({path});
				
				height: 100%;
				width: 100%;                             
				background-position: center;
				background-repeat: no-repeat;                           '''

class rpg_popup:
	def __init__(self, choose_option) -> None:
		self.setupUi(choose_option)

	def setupUi(self, choose_option:QMainWindow):
		choose_option.setObjectName("choose_option")
		choose_option.resize(598, 347)
		self.pushButton = QPushButton(choose_option)
		self.pushButton.setGeometry(QRect(90, 100, 161, 51))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(lambda: run_class(trainer_manager))
		self.pushButton_2 = QPushButton(choose_option)
		self.pushButton_2.setGeometry(QRect(350, 100, 161, 51))
		self.pushButton_2.setSizeIncrement(QSize(0, 0))
		self.pushButton_2.setBaseSize(QSize(0, 0))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_2.setAutoDefault(True)
		self.okbutton = QPushButton(choose_option)
		self.okbutton.setGeometry(QRect(210, 240, 191, 51))
		self.okbutton.setSizeIncrement(QSize(0, 0))
		self.okbutton.setBaseSize(QSize(0, 0))
		self.okbutton.setObjectName("okbutton")
		self.okbutton.clicked.connect(delete_win)
		global started
		if  os.path.exists(q:=os.path.join(cwd, 'rpg', 'game.save')):
			started = True
		if started:
			self.pushButton.setGeometry(QRect(50, 100, 161, 51))
			self.pushButton_2.setGeometry(QRect(390, 100, 161, 51))
			self.continuebutton = QPushButton(choose_option,text="continue")
			self.continuebutton.setGeometry(QRect(220, 100, 161, 51))
			self.continuebutton.setSizeIncrement(QSize(0, 0))
			self.continuebutton.setBaseSize(QSize(0, 0))
			self.continuebutton.setObjectName("continuebutton")
			self.continuebutton.clicked.connect(lambda :start_chess({}, True))

		self.menubar = QMenuBar(choose_option)
		self.menubar.setGeometry(QRect(0, 0, 598, 21))
		self.menubar.setObjectName("menubar")
		choose_option.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(choose_option)
		self.statusbar.setObjectName("statusbar")
		choose_option.setStatusBar(self.statusbar)

		self.retranslateUi(choose_option)
		QMetaObject.connectSlotsByName(choose_option)
		choose_option.show()
		
	def retranslateUi(self, choose_option):
		_translate = QCoreApplication.translate
		choose_option.setWindowTitle(_translate("choose_option", "AnkiNick-mon"))
		self.pushButton.setText(_translate("choose_option", "solo Adventure"))
		self.pushButton_2.setText(_translate("choose_option", "challenge a friend"))
		self.okbutton.setText(_translate("choose_option", "ok"))
		

def run_class(_class):
	mw.win = QMainWindow()
	_class(mw.win)




class attribute_popup:
	def __init__(self, win:QMainWindow):
		self.counter = 0
		# set the title
		self.things = []
		self.selected = [None for i in range(3)]
		win.setWindowTitle("AnkiNick-mon")        
		# setting the geometry of window
		win.setFixedSize(700,400)
		center_widget(win)
		data = get_data()
		self.Ankimons = ANKIMONS
		self.elements = ["Ice","Water","Fire"]
		self.tempwin = None
		self.buttons : list[QPushButton] = []
		self.dropdows : list[QComboBox] = []
		self.indexes = [2,2,2]
		self.selected_dropdows = [False for i in range(3)]
		for i in range(3):
			self.buttons.append(QPushButton(win))
			self.buttons[i].animateClick()
			self.buttons[i].setGeometry(70+i*200,70,150,150)
			self.dropdows.append(QComboBox(win))
			self.dropdows[i].addItems(self.elements)
			self.dropdows[i].setCurrentIndex(i)
			self.dropdows[i].activated.connect(partial(self.update_dropdowns,i))
			self.dropdows[i].move(95+i*200,250)
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
		self.okbutton = QPushButton(win,text="OK")
		self.okbutton.setGeometry(QRect(255, 320, 141, 51))
		self.okbutton.clicked.connect(self.ok)
		for index, dropdown in enumerate(self.dropdows):
			self.indexes[index] = dropdown.currentIndex()
			
		win.show()
	

	def update_dropdowns(self, index, i):
		# index is the number of the monster going left to right "i" is the index of the element they chose in the elements array
		self.indexes[index] = i


	def ok(self):
		for i in range(3):
			if self.indexes.count(i) > 1:
				utils.show_info('you can only choose each element once')
				return
		global started
		started = True
		dic = {self.selected[i]:self.elements[i] for i in range(3)}
		start_chess(dic)


	def clicked(self, index):
		self.counter += 1
		if self.counter > 3:	
			self.things.append(ankimon_selector(self, index))

	def update_ui(self):
		for i, button in enumerate(self.buttons):
			try:
				button.setStyleSheet(load_sheet(self.Ankimons.index(self.selected[i])))
				QPixmap(f"assets/heads/{self.selected[i]}.png")
				change_data("default_ankimon", self.selected)
			except TypeError as e:
				print(e)

class ankimon_selector(QMainWindow):
	def __init__(self, attribute: attribute_popup, index):
		super().__init__()
		self.ankimon_index = index
		# set the title
		self.attribute = attribute
		self.setWindowTitle("AnkiNick-mon")        
		# setting the geometry of window
		self.setFixedSize(840,580)
		center_widget(self)
		central_widget = self
		data = get_data()
		self.Ankimons = attribute.Ankimons
		self.buttons : list[QPushButton] = []
		labels : list[QLabel] = []
        # Create a scroll area
		self.counter = 0
		index = 0

		# show all the widgets
		self.completed = False
		scroll_area = QScrollArea()
		scroll_area.setWidgetResizable(True)

		# Create a widget and a layout for the scroll area
		# content_widget = QWidget()
		# content_layout = QGridLayout(content_widget)
		for i in range(len(self.Ankimons)):
			if self.Ankimons[i] not in self.attribute.selected:
				self.buttons.append(QPushButton(central_widget))
				text=str(Ankimons[i])
				labels.append(QLabel(parent=central_widget,text=text))
				width = labels[index].fontMetrics().boundingRect(labels[index].text()).width()
				labels[index].setGeometry(110+(index%4)*200-width/2,175+180*(index//4),150,150)
				labels[index].adjustSize()
				self.buttons[index].animateClick()
				self.buttons[index].setGeometry(40+(index%4)*200,20+180*(index//4),150,150)

				self.buttons[index].setStyleSheet(load_sheet(i))
				self.buttons[index].clicked.connect(partial(self.clicked,i))
				# content_layout.addWidget(labels[index])
				# content_layout.addWidget(self.buttons[index])
				index += 1
		
	

		# Set the widget with labels as the scroll area's widget
		# scroll_area.setWidget(content_widget)

		# # Set the scroll area as the central widget
		# self.setCentralWidget(content_widget)
		self.show()
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
			self.close()
			self.attribute.update_ui()
		self.counter += 1


class trainer_selector(QMainWindow):
	def __init__(self, attribute: attribute_popup, index):
		super().__init__()
		self.trainer_index = index
		# set the title
		self.attribute = attribute
		self.setWindowTitle("AnkiNick-mon")        
		# setting the geometry of window
		self.setFixedSize(840,580)
		center_widget(self)
		central_widget = self
		data = get_data()
		self.trainers = TRAINERS
		self.buttons : list[QPushButton] = []
		labels : list[QLabel] = []
        # Create a scroll area
		self.counter = 0
		index = 0

		# show all the widgets
		self.completed = False
		for i in range(len(self.trainers)):
			if self.trainers[i] not in self.attribute.selected:
				self.buttons.append(QPushButton(central_widget))
				text=str(self.trainers[i])
				labels.append(QLabel(parent=central_widget,text=text))
				width = labels[index].fontMetrics().boundingRect(labels[index].text()).width()
				labels[index].setGeometry(110+(index%4)*200-width/2,175+180*(index//4),150,150)
				labels[index].adjustSize()
				self.buttons[index].animateClick()
				self.buttons[index].setGeometry(40+(index%4)*200,20+180*(index//4),150,150)

				self.buttons[index].setStyleSheet(load_sheet(i, 'trainers', self.trainers))
				self.buttons[index].clicked.connect(partial(self.clicked,i))
				index += 1
		
	
		self.show()
		if self.completed:
			return

	def clicked(self, i):
		if self.counter > len(self.buttons)-1:
			try:
				self.attribute.selected[self.trainer_index] = self.trainers[i]
			except IndexError as e:
				print(e)
				self.attribute.selected.append(self.trainers[i])
			self.completed = True
			self.attribute.update_ui()
			
			self.attribute.things = []
			mw.win = QMainWindow()
			attribute_popup(mw.win)				
			self.close()

		self.counter += 1

class LoginHandler:
	def __init__(self, main_window:QMainWindow):
		self.main_window = main_window
		self.initUI()

	def initUI(self):
		# Set the main window properties
		self.main_window.setWindowTitle('Login')
		self.main_window.setFixedSize(280, 150)
		center_widget(self.main_window)
		# Create central widget
		self.central_widget = QWidget(self.main_window)
		self.main_window.setCentralWidget(self.central_widget)
		
		# Create layout
		layout = QVBoxLayout()
		
		# Create and add widgets to the layout
		self.label_username = QLabel('Username:', self.central_widget)
		layout.addWidget(self.label_username)
		
		self.textbox_username = QLineEdit(self.central_widget)
		layout.addWidget(self.textbox_username)
		
		self.label_password = QLabel('Password:', self.central_widget)
		layout.addWidget(self.label_password)
		
		self.textbox_password = QLineEdit(self.central_widget)
		layout.addWidget(self.textbox_password)
		
		self.button_login = QPushButton('Login', self.central_widget)
		self.button_login.clicked.connect(lambda :self.handle_login())
		layout.addWidget(self.button_login)
		
		# Set the layout on the central widget
		self.central_widget.setLayout(layout)
		self.main_window.show()
        
	def handle_login(self):
		username = self.textbox_username.text()
		password = self.textbox_password.text()
		print(username, password)
		# Perform your login logic here (this is a simple example)
		if username == "user" and password == "pass":
			QMessageBox.information(self.main_window, 'Login', 'Login successful!')
			self.textbox_username.clear()
			self.textbox_password.clear()
			delete_win()
			self.main_window = None
			from streakgame.main import main
			main()
			# Proceed to the next window or action
		else:
			QMessageBox.warning(self.main_window, 'Login', 'Incorrect username or password.')
			self.textbox_password.clear()

class trainer_manager:
	def __init__(self, win:QMainWindow):
		self.counter = 0
		# set the title
		self.things = []
		self.selected = [None]
		win.setWindowTitle("AnkiNick-mon")        
		# setting the geometry of window
		win.setFixedSize(700,400)
		center_widget(win)
		data = get_data()
		self.trainers = TRAINERS
		self.tempwin = None
		self.buttons : list[QPushButton] = []
		self.indexes = [2,2,2]
		for i in range(1):
			self.buttons.append(QPushButton(win))
			self.buttons[i].animateClick()
			self.buttons[i].setGeometry(70+1*200,70,150,150)
			self.buttons[i].setStyleSheet(f'''border-image : url(assets/ui/empty.PNG);
			
			height: 100%;
			width: 100%;                             
			background-position: center;
			background-repeat: no-repeat;                           ''')
			self.buttons[i].clicked.connect(partial(self.clicked,i))
		if data['default_trainer']:
			self.selected = [data['default_trainer']]
			self.update_ui()
		# show all the widgets
		self.okbutton = QPushButton(win,text="OK")
		self.okbutton.setGeometry(QRect(265, 320, 141, 51))
		self.okbutton.clicked.connect(self.ok)
			
		win.show()
	


	def ok(self):
		mw.win = QMainWindow()
		attribute_popup(mw.win)
		


	def clicked(self, index):
		self.counter += 1
		if self.counter > 1:	
			self.things.append(trainer_selector(self, index))
			

	def update_ui(self):
		print(self.selected)
		for i, button in enumerate(self.buttons):
			try:
				button.setStyleSheet(load_sheet(self.trainers.index(self.selected[i]), 'trainers', self.trainers))
				QPixmap(f"assets/trainers/{self.selected[i]}.png")
				change_data("default_trainer", self.selected[0])
				
				
			except Exception as e:
				print(e)
		


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    choose_option = QMainWindow()
    ui = rpg_popup()
    ui.setupUi(choose_option)
    choose_option.show()
    sys.exit(app.exec_())