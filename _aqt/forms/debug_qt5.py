# Form implementation generated from reading ui file 'qt/aqt/forms/debug.ui'
#
# Created by: PyQt5 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 582)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:anki.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.script = QtWidgets.QComboBox(parent=Dialog)
        self.script.setCurrentText("")
        self.script.setObjectName("script")
        self.verticalLayout.addWidget(self.script)
        self.splitter = QtWidgets.QSplitter(parent=Dialog)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.text = QtWidgets.QPlainTextEdit(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setMinimumSize(QtCore.QSize(0, 100))
        self.text.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.text.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap)
        self.text.setPlaceholderText("Actions:\n"
"    Ctrl+Enter          Execute\n"
"    Ctrl+Shift+Enter    Execute and print current line\n"
"    Ctrl+L              Clear log\n"
"    Ctrl+Shift+L        Clear input\n"
"    Ctrl+S              Save script\n"
"    Ctrl+O              Open script\n"
"    Ctrl+D              Delete script\n"
"\n"
"Locals:\n"
"    mw: AnkiQt                          Main window\n"
"    card: Callable[[], Card | None]     Reviewer card\n"
"    bcard: Callable[[], Card | None]    Browser card\n"
"    pp: Callable[[object], None]        Pretty print")
        self.text.setObjectName("text")
        self.log = QtWidgets.QPlainTextEdit(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setMinimumSize(QtCore.QSize(0, 150))
        self.log.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Output")
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.splitter)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setTitle("Styling")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetsButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.widgetsButton.setText("Qt Widget Gallery")
        self.widgetsButton.setObjectName("widgetsButton")
        self.verticalLayout_2.addWidget(self.widgetsButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        self.script.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.text, self.widgetsButton)
        Dialog.setTabOrder(self.widgetsButton, self.script)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.qt_misc_debug_console())