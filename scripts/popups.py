import requests.cookies
from scripts.utils import center_widget, get_data, change_data
import pickle
from aqt.qt import *
import webbrowser
import threading
from aqt import mw
from aqt import utils
from rpg.main import mainloop
from functools import partial
from enum import Enum
import json
from rpg.ankirpg import data_path, AnkiRPG
import random
import requests
from scripts.utils import xp_to_lvl
from scripts.constants import *

def delete_win():
    mw.win = None

def start_chess(ankimons:dict, load_save=False):
	delete_win()
	mw.web.eval("pycmd('study');")
	mainloop(ankimons, load_save)
started = False

Ankimons = UNLOCKED_ANKIMONS
def load_sheet(i, folder='heads', names:list[str]=Ankimons):
	cwd = os.getcwd()+os.sep[0]
	path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f"assets",folder,f"{names[i]}.png"if 'png' not in names[i].lower() else names[i]).replace(cwd, '').replace(os.sep[0],'/')
	print(path)
	return	f'''border-image : url({path});
				
				height: 100%;
				width: 100%;                             
				background-position: center;
				background-REPEAT: no-repeat;                           '''

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
		if  os.path.exists(q:=SAVE_PATH):
			print('save path exists')
			try:
				AnkiRPG.check()
				started = True
			except Exception as e:
				started = False
		else:
			started = False
			
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
		self.Ankimons = Ankimons
		self.elements = ["Ice","Water","Fire"]
		self.tempwin = None
		self.buttons : list[QPushButton] = []
		self.dropdows : list[QComboBox] = []
		self.indexes = [2,2,2]
		self.selected_dropdows = [False for i in range(3)]
		print(self.Ankimons)
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
			self.selected =  [anki for anki in data['default_ankimon'] if anki in self.Ankimons]
			self.update_ui()
		while len(self.selected) < 3:self.selected.append(None)
		# show all the widgets
		self.okbutton = QPushButton(win,text="OK")
		self.okbutton.setGeometry(QRect(255, 320, 141, 51))
		self.okbutton.clicked.connect(self.ok)
		for index, dropdown in enumerate(self.dropdows):
			self.indexes[index] = dropdown.currentIndex()
		print(self.selected)
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
		if all(dic.keys()):
			start_chess(dic)


	def clicked(self, index):
		self.counter += 1
		if self.counter > 3:	
			if [anki for anki in self.Ankimons if anki not in self.selected]:
				self.things.append(ankimon_selector(self, index))
			else:
				utils.showInfo('Unlock more ankimons to choose from')

	def update_ui(self):
		for i, button in enumerate(self.buttons):
			try:
				button.setStyleSheet(load_sheet(self.Ankimons.index(self.selected[i])))
				change_data("default_ankimon", self.selected)
			except Exception as e:
				button.setStyleSheet(load_sheet(0, 'ui', ['empty.PNG']))
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
		streak_data = json.load(open(streak_data_path, 'r'))
		for i in range(len(self.Ankimons)):
			if self.Ankimons[i] not in self.attribute.selected:
				self.buttons.append(QPushButton(central_widget))
				level= streak_data.get(Ankimons[i], '')
				if level: level = level.get('level', 1)
				else:level = 1
				labels.append(QLabel(parent=central_widget,text=f'Level {level}'))
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
		self.trainers = list(filter(lambda x:x not in STATS.keys() ,TRAINERS))
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
				labels[index].setGeometry(110+(index%4)*200-width/2,175+180*(index//4),130,150)
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
						
			self.close()

		self.counter += 1

class LoginHandler:
	def __init__(self, main_window: QMainWindow):
		self.main_window = main_window
		self.initUI()

	def initUI(self):
		# Set the main window properties
		self.main_window.setWindowTitle('Login')
		self.main_window.setFixedSize(280, 200)  # Increased height to accommodate the new button
		self.center_widget(self.main_window)

		# Create central widget
		self.central_widget = QWidget(self.main_window)
		self.main_window.setCentralWidget(self.central_widget)

		# Create layout
		layout = QVBoxLayout()

		# Create and add widgets to the layout
		self.label_username = QLabel('Email:', self.central_widget)
		layout.addWidget(self.label_username)

		self.textbox_username = QLineEdit(self.central_widget)
		layout.addWidget(self.textbox_username)

		self.label_password = QLabel('Password:', self.central_widget)
		layout.addWidget(self.label_password)

		self.textbox_password = QLineEdit(self.central_widget)
		self.textbox_password.setEchoMode(QLineEdit.EchoMode.Password)
		layout.addWidget(self.textbox_password)

		self.button_login = QPushButton('Login', self.central_widget)
		self.button_login.clicked.connect(self.handle_login)
		layout.addWidget(self.button_login)

		# Add "Create Account" button
		self.button_create_account = QPushButton('Create Account', self.central_widget)
		self.button_create_account.clicked.connect(lambda :self.open_create_account())
		layout.addWidget(self.button_create_account)

		# Set the layout on the central widget
		self.central_widget.setLayout(layout)
		self.main_window.show()

	def handle_login(self):
		username = self.textbox_username.text()
		password = self.textbox_password.text()
		print(username, password)
		data = {'email': username, 'password': password, 'device_name': 'python game'}
		res = requests.post('https://api.ankinick.org/login', json=data)
		# print(res.json())
		# print(f"cookies recived: {res.cookies.get_dict()}")
		# Perform your login logic here (this is a simple example)
		self.main_window.close()
		mw.win = None
		from streakgame import main
		main.main()


	def open_create_account(self):
		# URL of the website where the user can create an account
		webbrowser.open('https://api.ankinick.org/register')
	def center_widget(self, widget):
		qr = widget.frameGeometry()
		cp = widget.screen().availableGeometry().center()
		qr.moveCenter(cp)
		widget.move(qr.topLeft())

class trainer_manager:
	def __init__(self, win:QMainWindow):
		self.counter = 0
		# set the title
		self.things = []
		self.selected = [None]
		win.setWindowTitle("AnkiNick-mon")        
		self.ratio = .6
		# setting the geometry of window
		self.win = win
		win.setFixedSize(700,400)
		center_widget(win)
		data = get_data()
		self.label = QLabel(self.win)
		self.trainers = TRAINERS
		self.tempwin = None
		self.buttons : list[QPushButton] = []
		self.indexes = [2,2,2]
		self.item = data.get('item', None)
		print(data.get('trainer_xp', 0))
		self.level = xp_to_lvl(data.get('trainer_xp', 0))
		self.set_ratio(self.level%1)
		for i in range(2):
			self.buttons.append(QPushButton(win))
			self.buttons[i].animateClick()
			self.buttons[i].setGeometry(220+i*220,90+i*50,150-i*100,150-i*100+int(not i)*30)
			self.buttons[i].setStyleSheet(f'''border-image : url(assets/ui/empty.PNG);
			
			height: 100%;
			width: 100%;                             
			background-position: center;
			background-repeat: no-repeat;                           ''')
			self.buttons[i].clicked.connect(partial(self.clicked,i))
		if data.get('default_trainer', None):
			self.selected = [data['default_trainer']]
			self.update_ui()

		# show all the widgets
		self.okbutton = QPushButton(win,text="OK")
		self.okbutton.setGeometry(QRect(265, 320, 141, 51))
		self.okbutton.clicked.connect(self.ok)
		self.win.paintEvent = self.paintEvent			
		win.show()
	

	def set_ratio(self, ratio):
		"""Sets the health ratio and updates the display."""
		self.ratio = max(0, min(1, ratio))  # Ensure ratio is between 0 and 1
		self.label.setText(f"lvl{int(self.level)}")
		self.label.move(int(self.win.width()//2.5),5)
		self.label.setFont(QFont(self.label.font().toString(),15))
		self.win.update()  # Trigger a repaint

	def paintEvent(self, event):
		painter = QPainter(self.win)
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)

		# Get current window size
		current_width = self.win.width()//4
		current_height = 20
		# Draw a border around the health bar
		painter.setPen(QColor(0, 0, 0))
		painter.drawRect(current_width*1.2, 40, current_width-1, current_height-1)
		# Draw foreground (filled part of the health bar based on ratio)
		painter.setBrush(QBrush(Qt.GlobalColor.green))
		filled_width = current_width * self.ratio
		painter.drawRect(current_width*1.2, 40, filled_width, current_height)


	def ok(self):
		self.win.close()
		mw.win = QMainWindow()
		attribute_popup(mw.win)
		


	def clicked(self, index):
		self.counter += 1
		if self.counter > len(self.buttons):	
			if not get_data()['default_trainer']:
				self.things.append(trainer_selector(self, index))
			if index == 1:
				self.things.append(item_selector(self, index))		
			

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
		
class item_selector(QMainWindow):
	def __init__(self, attribute: trainer_manager, index):
		super().__init__()
		self.item_index = index
		# set the title
		self.attribute = attribute
		self.setWindowTitle("AnkiNick-mon")        
		# setting the geometry of window
		self.setFixedSize(840,580)
		center_widget(self)
		central_widget = self
		data = get_data()
		self.items = ITEMS
		self.buttons : list[QPushButton] = []
		labels : list[QLabel] = []
        # Create a scroll area
		self.counter = 0
		index = 0

		# show all the widgets
		self.completed = False
		for i in range(len(self.items)):
			if self.items[i] not in self.attribute.selected:
				self.buttons.append(QPushButton(central_widget))
				text=str(self.items[i])
				labels.append(QLabel(parent=central_widget,text=text))
				width = labels[index].fontMetrics().boundingRect(labels[index].text()).width()
				labels[index].setGeometry(110+(index%4)*200-width/2,175+180*(index//4),150,150)
				labels[index].adjustSize()
				self.buttons[index].animateClick()
				self.buttons[index].setGeometry(40+(index%4)*200,20+180*(index//4),150,150)

				self.buttons[index].setStyleSheet(load_sheet(i, 'items', self.items))
				self.buttons[index].clicked.connect(partial(self.clicked,i))
				index += 1
		
	
		self.show()
		if self.completed:
			return

	def clicked(self, i):
		if self.counter > len(self.buttons)-1:
				self.attribute.item = self.items[i]
				self.attribute.update_ui()
				self.close()
				self.attribute.selected.append(self.items[i])
			

		self.counter += 1

class Difficulties(Enum):
	Easy = 0.5
	Normal = 1
	Hard = 2
	Expert = 3

class DifficultyChoosingWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle('Choose Difficulty')
		self.setGeometry(100, 100, 400, 300)
		center_widget(self)
		self.initUI()
		
	def initUI(self):
		# Main widget
		widget = QWidget()
		self.setCentralWidget(widget)
		
		# Layout
		layout = QVBoxLayout()
		
		# Label
		label = QLabel("Select Your Difficulty Level", self)
		label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		label.setFont(QFont('Arial', 24))
		label.setStyleSheet("color: #FFFFFF; margin-bottom: 20px;")
		layout.addWidget(label)
		
		# Button styles
		button_style = """
			QPushButton {
				background-color: #3A3A3A;
				color: #FFFFFF;
				font-size: 18px;
				font-family: Arial;
				padding: 10px;
				border-radius: 10px;
				margin: 10px 0;
			}
			QPushButton:hover {
				background-color: #5A5A5A;
			}
			QPushButton:pressed {
				background-color: #2A2A2A;
			}
		"""
		
		# Buttons
		easy_button = QPushButton('Easy', self)
		medium_button = QPushButton('Medium', self)
		hard_button = QPushButton('Hard', self)
		expert_button = QPushButton('Expert', self)
		
		easy_button.setStyleSheet(button_style)
		medium_button.setStyleSheet(button_style)
		hard_button.setStyleSheet(button_style)
		expert_button.setStyleSheet(button_style)
		
		# Connect buttons to functions
		easy_button.clicked.connect(lambda: self.choose_difficulty(Difficulties.Easy))
		medium_button.clicked.connect(lambda: self.choose_difficulty(Difficulties.Normal))
		hard_button.clicked.connect(lambda: self.choose_difficulty(Difficulties.Hard))
		expert_button.clicked.connect(lambda: self.choose_difficulty(Difficulties.Expert))
		
		# Add buttons to layout
		layout.addWidget(easy_button)
		layout.addWidget(medium_button)
		layout.addWidget(hard_button)
		layout.addWidget(expert_button)
		
		widget.setLayout(layout)
		
		# Set background color
		palette = QPalette()
		palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
		self.setPalette(palette)
		self.show()
		
	def choose_difficulty(self, difficulty:Difficulties):
		print(f'Difficulty chosen: {difficulty}')
        # Save the difficulty to the JSON file and close the window.
		change_data('Difficulty', difficulty.value)
		self.close()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    choose_option = QMainWindow()
    ui = rpg_popup()
    ui.setupUi(choose_option)
    choose_option.show()
    sys.exit(app.exec_())