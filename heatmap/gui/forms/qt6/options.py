# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 530)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutBanner = QtWidgets.QHBoxLayout()
        self.layoutBanner.setObjectName("layoutBanner")
        self.labHeading = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labHeading.setFont(font)
        self.labHeading.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labHeading.setIndent(2)
        self.labHeading.setObjectName("labHeading")
        self.layoutBanner.addWidget(self.labHeading)
        self.verticalLayout.addLayout(self.layoutBanner)
        self.layoutSocialBtns = QtWidgets.QHBoxLayout()
        self.layoutSocialBtns.setObjectName("layoutSocialBtns")
        self.labDebug = QtWidgets.QLabel(parent=Dialog)
        self.labDebug.setText("")
        self.labDebug.setObjectName("labDebug")
        self.layoutSocialBtns.addWidget(self.labDebug)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layoutSocialBtns.addItem(spacerItem)
        self.fmtLabInfo = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.fmtLabInfo.setFont(font)
        self.fmtLabInfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fmtLabInfo.setObjectName("fmtLabInfo")
        self.layoutSocialBtns.addWidget(self.fmtLabInfo)
        self.verticalLayout.addLayout(self.layoutSocialBtns)
        self.tabWidget = QtWidgets.QTabWidget(parent=Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contribLayout = QtWidgets.QVBoxLayout()
        self.contribLayout.setContentsMargins(-1, 10, -1, 5)
        self.contribLayout.setObjectName("contribLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.labHeart = QtWidgets.QLabel(parent=self.tab)
        self.labHeart.setText("")
        self.labHeart.setPixmap(QtGui.QPixmap(":/review_heatmap/icons/heart.svg"))
        self.labHeart.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labHeart.setObjectName("labHeart")
        self.horizontalLayout_3.addWidget(self.labHeart)
        self.fmtLabContrib = QtWidgets.QLabel(parent=self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fmtLabContrib.setFont(font)
        self.fmtLabContrib.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fmtLabContrib.setObjectName("fmtLabContrib")
        self.horizontalLayout_3.addWidget(self.fmtLabContrib)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.contribLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.contribLayout.addLayout(self.gridLayout_3)
        self.label_5 = QtWidgets.QLabel(parent=self.tab)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/review_heatmap/icons/thanks.svg"))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.contribLayout.addWidget(self.label_5)
        self.verticalLayout_5.addLayout(self.contribLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem5)
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.selHmColor = QtWidgets.QComboBox(parent=self.groupBox)
        self.selHmColor.setObjectName("selHmColor")
        self.gridLayout.addWidget(self.selHmColor, 0, 1, 1, 1)
        self.selHmCalMode = QtWidgets.QComboBox(parent=self.groupBox)
        self.selHmCalMode.setObjectName("selHmCalMode")
        self.gridLayout.addWidget(self.selHmCalMode, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbHmMain = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.cbHmMain.setObjectName("cbHmMain")
        self.horizontalLayout.addWidget(self.cbHmMain)
        self.cbHmDeck = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.cbHmDeck.setObjectName("cbHmDeck")
        self.horizontalLayout.addWidget(self.cbHmDeck)
        self.cbHmStats = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.cbHmStats.setObjectName("cbHmStats")
        self.horizontalLayout.addWidget(self.cbHmStats)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbStreakAll = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.cbStreakAll.setObjectName("cbStreakAll")
        self.verticalLayout_4.addWidget(self.cbStreakAll)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinLimFcst = QtWidgets.QSpinBox(parent=self.tab_2)
        self.spinLimFcst.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.spinLimFcst.setMinimum(0)
        self.spinLimFcst.setMaximum(1000000)
        self.spinLimFcst.setObjectName("spinLimFcst")
        self.gridLayout_2.addWidget(self.spinLimFcst, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setToolTip("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.dateLimData = QtWidgets.QDateEdit(parent=self.tab_2)
        self.dateLimData.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dateLimData.setMinimumDate(QtCore.QDate(2006, 10, 5))
        self.dateLimData.setCalendarPopup(True)
        self.dateLimData.setObjectName("dateLimData")
        self.gridLayout_2.addWidget(self.dateLimData, 1, 1, 1, 1)
        self.spinLimHist = QtWidgets.QSpinBox(parent=self.tab_2)
        self.spinLimHist.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.spinLimHist.setMinimum(0)
        self.spinLimHist.setMaximum(1000000)
        self.spinLimHist.setObjectName("spinLimHist")
        self.gridLayout_2.addWidget(self.spinLimHist, 2, 1, 1, 1)
        self.cbLimDel = QtWidgets.QCheckBox(parent=self.tab_2)
        self.cbLimDel.setObjectName("cbLimDel")
        self.gridLayout_2.addWidget(self.cbLimDel, 4, 0, 1, 2)
        self.cbLimResched = QtWidgets.QCheckBox(parent=self.tab_2)
        self.cbLimResched.setObjectName("cbLimResched")
        self.gridLayout_2.addWidget(self.cbLimResched, 5, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 10)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem7)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listDecks = QtWidgets.QListWidget(parent=self.groupBox_2)
        self.listDecks.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listDecks.setObjectName("listDecks")
        self.horizontalLayout_4.addWidget(self.listDecks)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btnDeckAdd = QtWidgets.QToolButton(parent=self.groupBox_2)
        self.btnDeckAdd.setMinimumSize(QtCore.QSize(32, 0))
        self.btnDeckAdd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/review_heatmap/icons/plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDeckAdd.setIcon(icon)
        self.btnDeckAdd.setIconSize(QtCore.QSize(16, 16))
        self.btnDeckAdd.setObjectName("btnDeckAdd")
        self.verticalLayout_7.addWidget(self.btnDeckAdd)
        self.btnDeckDel = QtWidgets.QToolButton(parent=self.groupBox_2)
        self.btnDeckDel.setMinimumSize(QtCore.QSize(32, 0))
        self.btnDeckDel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/review_heatmap/icons/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDeckDel.setIcon(icon1)
        self.btnDeckDel.setObjectName("btnDeckDel")
        self.verticalLayout_7.addWidget(self.btnDeckDel)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.htmlAbout = QtWidgets.QTextBrowser(parent=self.tab_3)
        self.htmlAbout.setOpenExternalLinks(True)
        self.htmlAbout.setOpenLinks(False)
        self.htmlAbout.setObjectName("htmlAbout")
        self.verticalLayout_3.addWidget(self.htmlAbout)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok|QtWidgets.QDialogButtonBox.StandardButton.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.selHmColor)
        self.label_2.setBuddy(self.selHmCalMode)
        self.label_3.setBuddy(self.spinLimHist)
        self.label_4.setBuddy(self.spinLimFcst)
        self.label_7.setBuddy(self.dateLimData)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.selHmColor)
        Dialog.setTabOrder(self.selHmColor, self.selHmCalMode)
        Dialog.setTabOrder(self.selHmCalMode, self.cbHmMain)
        Dialog.setTabOrder(self.cbHmMain, self.cbHmDeck)
        Dialog.setTabOrder(self.cbHmDeck, self.cbHmStats)
        Dialog.setTabOrder(self.cbHmStats, self.cbStreakAll)
        Dialog.setTabOrder(self.cbStreakAll, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.dateLimData)
        Dialog.setTabOrder(self.dateLimData, self.spinLimHist)
        Dialog.setTabOrder(self.spinLimHist, self.spinLimFcst)
        Dialog.setTabOrder(self.spinLimFcst, self.cbLimDel)
        Dialog.setTabOrder(self.cbLimDel, self.listDecks)
        Dialog.setTabOrder(self.listDecks, self.btnDeckAdd)
        Dialog.setTabOrder(self.btnDeckAdd, self.btnDeckDel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Review Heatmap Settings"))
        self.labHeading.setText(_translate("Dialog", "Review Heatmap Settings"))
<<<<<<< HEAD
=======
        self.btnHelp.setText(_translate("Dialog", "?"))
        self.btnHelp.setShortcut(_translate("Dialog", "Ctrl+H"))
>>>>>>> b86aea5afbad61626476e5f9e39c6ff713681b2a
        self.fmtLabInfo.setText(_translate("Dialog", "<a href=\"action://changelog\">v{ADDON_VERSION}</a>"))
        self.fmtLabContrib.setText(_translate("Dialog", "Review Heatmap?"))
        self.groupBox.setTitle(_translate("Dialog", "Heatmap appearance"))
        self.label.setText(_translate("Dialog", "Co&lor scheme"))
        self.label_2.setText(_translate("Dialog", "Calendar &mode"))
        self.selHmColor.setToolTip(_translate("Dialog", "Sets the general color scheme of the add-on"))
        self.selHmCalMode.setToolTip(_translate("Dialog", "Sets the display mode of the calendar"))
        self.groupBox_3.setTitle(_translate("Dialog", "Heatmap visibility"))
        self.cbHmMain.setToolTip(_translate("Dialog", "Screen you\'re presented with when starting Anki"))
        self.cbHmMain.setText(_translate("Dialog", "Mai&n screen"))
        self.cbHmDeck.setToolTip(_translate("Dialog", "Screen you see when clicking on a deck from the main screen"))
        self.cbHmDeck.setText(_translate("Dialog", "Dec&k screen"))
        self.cbHmStats.setToolTip(_translate("Dialog", "Stats window"))
        self.cbHmStats.setText(_translate("Dialog", "Sta&ts screen"))
        self.groupBox_4.setTitle(_translate("Dialog", "Streak visibility"))
        self.cbStreakAll.setToolTip(_translate("Dialog", "<html>Overrides the heatmap visibility setting, always showing you information on your stats (e.g. streaks, average, etc.)</html>"))
        self.cbStreakAll.setText(_translate("Dialog", "Show streak &stats even when heatmap disabled"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "&General"))
        self.spinLimFcst.setToolTip(_translate("Dialog", "<html>Limits the number of days in the future that the heatmap displays. Only applies to main screen and deck overview.</html>"))
        self.spinLimFcst.setSpecialValueText(_translate("Dialog", "No limit"))
        self.spinLimFcst.setSuffix(_translate("Dialog", " days"))
        self.label_3.setText(_translate("Dialog", "&History limit"))
        self.label_4.setText(_translate("Dialog", "Fore&cast limit"))
        self.label_7.setText(_translate("Dialog", "&Ignore data before"))
        self.dateLimData.setToolTip(_translate("Dialog", "<html>Allows you to exclude a period of time from your stats (e.g. when you were still getting familiar with Anki).<br>Only applies to main screen and deck overview.</html>"))
        self.spinLimHist.setToolTip(_translate("Dialog", "<html>Limits the number of days in the past that the heatmap displays. Only applies to main screen and deck overview.</html>"))
        self.spinLimHist.setSpecialValueText(_translate("Dialog", "No limit"))
        self.spinLimHist.setSuffix(_translate("Dialog", " days"))
        self.cbLimDel.setToolTip(_translate("Dialog", "<html>Ignores any reviews performed of cards that have been deleted since</html>"))
        self.cbLimDel.setText(_translate("Dialog", "&Exclude deleted cards from history"))
        self.cbLimResched.setText(_translate("Dialog", "Exclude manual reschedules from history"))
        self.groupBox_2.setTitle(_translate("Dialog", "Exclude decks from main heatmap:"))
        self.listDecks.setToolTip(_translate("Dialog", "<html>Any decks listed here will not be included in the calculations for the main heatmap. Each individual deck\'s heatmap will still work, however.</html>"))
        self.listDecks.setSortingEnabled(True)
        self.btnDeckAdd.setToolTip(_translate("Dialog", "Add new deck exclusion rule"))
        self.btnDeckAdd.setShortcut(_translate("Dialog", "Ctrl+D"))
        self.btnDeckDel.setToolTip(_translate("Dialog", "Delete deck exclusion rule"))
        self.btnDeckDel.setShortcut(_translate("Dialog", "Ctrl+Del, Ctrl+S"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "&Fine Tuning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "A&bout"))
