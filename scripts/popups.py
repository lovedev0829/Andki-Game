
from aqt.qt import *
from aqt import mw
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
def delete_win():
    mw.win = None
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    choose_option = QMainWindow()
    ui = rpg_popup()
    ui.setupUi(choose_option)
    choose_option.show()
    sys.exit(app.exec_())
