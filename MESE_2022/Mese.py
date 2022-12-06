﻿
## by karton4ik

#python -m PyQt6.uic.pyuic -x [FILENAME].ui -o [FILENAME].py

from PyQt6 import QtCore, QtGui, QtWidgets
from Dialog_Setup import Ui_Dialog_Setup
from Dialog_Restart import Ui_Dialog_Restart
from Dialog_Change_Level_of_Play import Ui_Dialog_Change_Level_of_Play
from Dialog_setParameters import Ui_Dialog_setParameters
from Dialog_SelectaCompany import Ui_Dialog_EnterallDecisions
from Dialog_SelectCompany_Review import Ui_Dialog_ReviewDecisions
from Dialog_ClosePeriod_Error import Ui_Dialog_ClosePeriod_Error
from Dialog_ClosePeriod import Ui_Dialog_ClosePeriod
from Dialog_Print import Ui_Dialog_Print
from Dialog_Contactus import Ui_Dialog_Contactus
from ast import literal_eval
import matplotlib.pyplot as mtbpt
import numpy as np

class Ui_Mese(object):
    
    def setupUi(self, Mese): 
        self.result = open("result.txt", "r").readline()
        self.result_literal_eval = None
        self.period = 0
        if self.result == "":
            self.period = 0
        else:
            self.result_literal_eval = literal_eval(self.result)
            self.period = self.result_literal_eval["now_tick"]
        Mese.setObjectName("Mese")
        Mese.setEnabled(True)
        Mese.resize(811, 543)
        Mese.setMinimumSize(QtCore.QSize(811, 543))
        Mese.setMaximumSize(QtCore.QSize(811, 543))
        Mese.setMouseTracking(False)
        Mese.setTabletTracking(False)
        Mese.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        Mese.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Mese.setWindowIcon(icon)
        Mese.setStatusTip("")
        Mese.setWhatsThis("")
        
        Mese.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Mese)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_Setup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Setup.setGeometry(QtCore.QRect(40, 240, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Setup.setFont(font)
        self.pushButton_Setup.setObjectName("pushButton_Setup")
        self.pushButton_Setup.clicked.connect(self.open_Setup)
        
        
        self.pushButton_Restart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Restart.setGeometry(QtCore.QRect(40, 320, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Restart.setFont(font)
        self.pushButton_Restart.setObjectName("pushButton_Restart")
        self.pushButton_Restart.clicked.connect(self.open_Restart)
        
        
        self.label_Simulation = QtWidgets.QLabel(self.centralwidget)
        self.label_Simulation.setGeometry(QtCore.QRect(60, 160, 131, 21))
        self.label_Simulation.setMaximumSize(QtCore.QSize(141, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_Simulation.setFont(font)
        self.label_Simulation.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.label_Simulation.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_Simulation.setScaledContents(False)
        self.label_Simulation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Simulation.setWordWrap(False)
        self.label_Simulation.setIndent(-1)
        self.label_Simulation.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_Simulation.setObjectName("label_Simulation")
        
        
        self.label_ResultsforPeriod = QtWidgets.QLabel(self.centralwidget)
        self.label_ResultsforPeriod.setGeometry(QtCore.QRect(560, 160, 180, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(13)
        self.label_ResultsforPeriod.setFont(font)
        
        self.result_period = self.period
        if self.period - 1 <= -1:
            self.result_period = ""
            
        self.label_ResultsforPeriod.setObjectName("label_ResultsforPeriod")
        
        
        self.label_DecisionsforPeriod = QtWidgets.QLabel(self.centralwidget)
        self.label_DecisionsforPeriod.setGeometry(QtCore.QRect(300, 150, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(13)
        self.label_DecisionsforPeriod.setFont(font)
        self.label_DecisionsforPeriod.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_DecisionsforPeriod.setObjectName("label_DecisionsforPeriod")
        
        
        self.pushButton_EnterallDecisions = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EnterallDecisions.setGeometry(QtCore.QRect(310, 200, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EnterallDecisions.setFont(font)
        self.pushButton_EnterallDecisions.setObjectName("pushButton_EnterallDecisions")
        self.pushButton_EnterallDecisions.clicked.connect(self.pushButton_EnterallDecisions_was_clicked)
        
        if self.period == 0:
            self.pushButton_EnterallDecisions.setEnabled(False)
        else:
            self.pushButton_EnterallDecisions.setEnabled(True)
        
        self.pushButton_ReviewDecisions = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ReviewDecisions.setGeometry(QtCore.QRect(310, 240, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ReviewDecisions.setFont(font)
        self.pushButton_ReviewDecisions.setObjectName("pushButton_ReviewDecisions")
        self.pushButton_ReviewDecisions.clicked.connect(self.pushButton_ReviewDecisions_was_clicked)
        
        if self.period == 0:
            self.pushButton_ReviewDecisions.setEnabled(False)
        else:
            self.pushButton_ReviewDecisions.setEnabled(True)
        
        self.pushButton_ClosePeriod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ClosePeriod.setGeometry(QtCore.QRect(310, 320, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ClosePeriod.setFont(font)
        self.pushButton_ClosePeriod.setObjectName("pushButton_ClosePeriod")
        self.pushButton_ClosePeriod.clicked.connect(self.pushButton_ClosePeriod_was_clicked)
        
        
        #self.pushButton_SelectPeriod = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_SelectPeriod.setGeometry(QtCore.QRect(570, 200, 161, 41))
        #font = QtGui.QFont()
        #font.setBold(True)
        #font.setWeight(75)
        #self.pushButton_SelectPeriod.setFont(font)
        #self.pushButton_SelectPeriod.setObjectName("pushButton_SelectPeriod")
        #self.pushButton_SelectPeriod.clicked.connect(self.pushButton_SelectPeriod_was_clicked)
        
        
        
        self.pushButton_View = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_View.setGeometry(QtCore.QRect(570, 200, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_View.setFont(font)
        self.pushButton_View.setObjectName("pushButton_View")
        self.pushButton_View.clicked.connect(self.pushButton_View_was_clicked)
        
        if self.period == 0:
            self.pushButton_View.setEnabled(False)
        else:
            self.pushButton_View.setEnabled(True)

        
        self.pushButton_Graph = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Graph.setGeometry(QtCore.QRect(570, 240, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Graph.setFont(font)
        self.pushButton_Graph.setObjectName("pushButton_Graph")
        self.pushButton_Graph.clicked.connect(self.pushButton_Graph_was_clicked)
        
        if self.period == 0:
            self.pushButton_Graph.setEnabled(False)
        else:
            self.pushButton_Graph.setEnabled(True)
        
        self.pushButton_Print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Print.setGeometry(QtCore.QRect(570, 320, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Print.setFont(font)
        self.pushButton_Print.setObjectName("pushButton_Print")
        self.pushButton_Print.clicked.connect(self.pushButton_Print_was_clicked)
        
        if self.period == 0:
            self.pushButton_Print.setEnabled(False)
        else:
            self.pushButton_Print.setEnabled(True)
        
        
        self.label_Options = QtWidgets.QLabel(self.centralwidget)
        self.label_Options.setGeometry(QtCore.QRect(80, 370, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(13)
        self.label_Options.setFont(font)
        self.label_Options.setObjectName("label_Options")
        
        
        self.pushButton_SetParameters = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SetParameters.setGeometry(QtCore.QRect(40, 450, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SetParameters.setFont(font)
        self.pushButton_SetParameters.setObjectName("pushButton_SetParameters")
        self.pushButton_SetParameters.clicked.connect(self.pushButton_SetParameters_was_clicked)
        
        
        self.pushButton_ChangeLevelOfPlay = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ChangeLevelOfPlay.setGeometry(QtCore.QRect(40, 410, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ChangeLevelOfPlay.setFont(font)
        self.pushButton_ChangeLevelOfPlay.setObjectName("pushButton_ChangeLevelOfPlay")
        self.pushButton_ChangeLevelOfPlay.clicked.connect(self.pushButton_ChangeLevelOfPlay_was_clicked)
        
        
        self.label_company = QtWidgets.QLabel(self.centralwidget)
        self.label_company.setGeometry(QtCore.QRect(730, 480, 141, 31))
        self.label_company.setObjectName("label_company")
        
        
        self.label_Version = QtWidgets.QLabel(self.centralwidget)
        self.label_Version.setGeometry(QtCore.QRect(750, 0, 61, 20))
        self.label_Version.setObjectName("label_Version")
        
        
        self.label_currentPeriod = QtWidgets.QLabel(self.centralwidget)
        self.label_currentPeriod.setGeometry(QtCore.QRect(40, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_currentPeriod.setFont(font)
        self.label_currentPeriod.setObjectName("label_currentPeriod")
        
        
        self.img_theFirstp = QtWidgets.QLabel(self.centralwidget)
        self.img_theFirstp.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.img_theFirstp.setText("")
        self.img_theFirstp.setPixmap(QtGui.QPixmap("Images/medal.png"))
        self.img_theFirstp.setScaledContents(True)
        self.img_theFirstp.setObjectName("img_theFirstp")
        
        
        self.img_theSecondp = QtWidgets.QLabel(self.centralwidget)
        self.img_theSecondp.setGeometry(QtCore.QRect(10, 100, 20, 20))
        self.img_theSecondp.setText("")
        self.img_theSecondp.setPixmap(QtGui.QPixmap("Images/medal (1).png"))
        self.img_theSecondp.setScaledContents(True)
        self.img_theSecondp.setObjectName("img_theSecondp")
        
        
        self.img_theThirdp = QtWidgets.QLabel(self.centralwidget)
        self.img_theThirdp.setGeometry(QtCore.QRect(10, 130, 20, 20))
        self.img_theThirdp.setText("")
        self.img_theThirdp.setPixmap(QtGui.QPixmap("Images/medal (2).png"))
        self.img_theThirdp.setScaledContents(True)
        self.img_theThirdp.setObjectName("img_theThirdp")
        
        
        self.label_theFirstp = QtWidgets.QLabel(self.centralwidget)
        self.label_theFirstp.setGeometry(QtCore.QRect(40, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        self.label_theFirstp.setFont(font)
        self.label_theFirstp.setObjectName("label_theFirstp")
        
        
        self.label_theSecondp = QtWidgets.QLabel(self.centralwidget)
        self.label_theSecondp.setGeometry(QtCore.QRect(40, 100, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        self.label_theSecondp.setFont(font)
        self.label_theSecondp.setObjectName("label_theSecondp")
        
        
        self.label_theThirdp = QtWidgets.QLabel(self.centralwidget)
        self.label_theThirdp.setGeometry(QtCore.QRect(40, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        self.label_theThirdp.setFont(font)
        self.label_theThirdp.setObjectName("label_theThirdp")
        
        
        Mese.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(Mese)
        self.statusbar.setObjectName("statusbar")
        
        
        Mese.setStatusBar(self.statusbar)
        
        self.menubar = QtWidgets.QMenuBar(Mese)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        
        
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        
        self.menuLanguage = QtWidgets.QMenu(self.menuOptions)
        self.menuLanguage.setTabletTracking(False)
        self.menuLanguage.setWhatsThis("")
        self.menuLanguage.setObjectName("menuLanguage")
        
        self.menuTheme = QtWidgets.QMenu(self.menuOptions)
        self.menuTheme.setObjectName("menuTheme")
        
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Mese.setMenuBar(self.menubar)
        
        self.actionEnglish = QtGui.QAction(Mese)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setChecked(True)
        self.actionEnglish.setShortcutVisibleInContextMenu(False)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionEnglish.triggered.connect(self.actionEnglish_was_clicked)
        
        self.action_Rus = QtGui.QAction(Mese)
        self.action_Rus.setCheckable(True)
        self.action_Rus.setObjectName("action_Rus")
        self.action_Rus.triggered.connect(self.action_Rus_was_clicked)
        
        self.actionDark = QtGui.QAction(Mese)
        self.actionDark.setCheckable(True)
        self.actionDark.setObjectName("actionDark")
        self.actionDark.triggered.connect(self.actionDark_was_clicked)
        
        self.actionLight = QtGui.QAction(Mese)
        self.actionLight.setCheckable(True)
        self.actionLight.setObjectName("actionLight")
        self.actionLight.triggered.connect(self.actionLight_was_clicked)
        
        self.actionContact_us = QtGui.QAction(Mese)
        self.actionContact_us.setObjectName("actionContact_us")
        self.actionContact_us.triggered.connect(self.actionContact_us_was_clicked)
        
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.action_Rus)
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionLight)
        self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.menuTheme.menuAction())
        self.menuHelp.addAction(self.actionContact_us)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        #self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #self.comboBox.setGeometry(QtCore.QRect(720, 160, 51, 22))
        #font = QtGui.QFont()
        #font.setFamily("Montserrat Medium")
        #font.setPointSize(13)
        #self.comboBox.setFont(font)
        #self.comboBox.setObjectName("comboBox")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        
        

        self.retranslateUi(Mese)
        QtCore.QMetaObject.connectSlotsByName(Mese)

        open("ClosePeriod_log.txt", "w").close()
        
        
        
    def retranslateUi(self, Mese):
        _translate = QtCore.QCoreApplication.translate
        Mese.setWindowTitle(_translate("Mese", "Mese"))
        self.pushButton_Setup.setText(_translate("Mese", "Setup"))
        self.pushButton_Restart.setText(_translate("Mese", "Restart"))
        self.label_Simulation.setText(_translate("Mese", "Simulation", "30"))
        self.label_ResultsforPeriod.setText(_translate("Mese", f"Results for Period {self.result_period}"))
        self.label_DecisionsforPeriod.setText(_translate("Mese", f"Decisions for Period {self.period}"))
        self.pushButton_EnterallDecisions.setText(_translate("Mese", "Enter all Decisions"))
        self.pushButton_ReviewDecisions.setText(_translate("Mese", "Review Decisions"))
        self.pushButton_ClosePeriod.setText(_translate("Mese", "Close Period"))
        #self.pushButton_SelectPeriod.setText(_translate("Mese", "Select Period"))
        self.pushButton_View.setText(_translate("Mese", "View"))
        self.pushButton_Graph.setText(_translate("Mese", "Graph"))
        self.pushButton_Print.setText(_translate("Mese", "Print"))
        self.label_Options.setText(_translate("Mese", "Options"))
        self.pushButton_SetParameters.setText(_translate("Mese", "Set Parameters"))
        self.pushButton_ChangeLevelOfPlay.setText(_translate("Mese", "Change Level of Play"))
        self.label_company.setText(_translate("Mese", "2022 TON corp."))
        self.label_Version.setText(_translate("Mese", "v0.1 Alpha"))
        self.label_currentPeriod.setText(_translate("Mese", f"Period {self.period}"))
        self.label_theFirstp.setText(_translate("Mese", "TONCHIK"))
        self.label_theSecondp.setText(_translate("Mese", "TONCHIK"))
        self.label_theThirdp.setText(_translate("Mese", "TONCHIK"))
        self.menuOptions.setTitle(_translate("Mese", "Options"))
        self.menuLanguage.setTitle(_translate("Mese", "Language"))
        self.menuTheme.setTitle(_translate("Mese", "Theme"))
        self.menuHelp.setTitle(_translate("Mese", "Help"))
        self.actionEnglish.setText(_translate("Mese", "English"))
        self.action_Rus.setText(_translate("Mese", "Русский"))
        self.actionDark.setText(_translate("Mese", "Dark"))
        self.actionLight.setText(_translate("Mese", "Light"))
        self.actionContact_us.setText(_translate("Mese", "Contact us"))
        #self.comboBox.setItemText(0, _translate("Mese", "1"))
        #self.comboBox.setItemText(1, _translate("Mese", "99"))
        #self.comboBox.setItemText(2, _translate("Mese", "2"))
    
    def open_Setup(self):
        self.Dialog_Setup = QtWidgets.QDialog()
        self.Dialog_Setup_ui = Ui_Dialog_Setup()   
        self.Dialog_Setup_ui.setupUi(self.Dialog_Setup)
        self.Dialog_Setup.exec()

    
    def open_Restart(self):
        self.Dialog_Restart = QtWidgets.QDialog()
        self.Dialog_Restart_ui = Ui_Dialog_Restart()
        self.Dialog_Restart_ui.setupUi(self.Dialog_Restart)
        self.Dialog_Restart.exec()
        
        with open("result.txt", "r") as f:
            if f.readline() == "":
                self.period = 0
                self.pushButton_EnterallDecisions.setEnabled(False)
                self.pushButton_ReviewDecisions.setEnabled(False)
                self.pushButton_View.setEnabled(False)
                self.pushButton_Graph.setEnabled(False)
                self.pushButton_Print.setEnabled(False)
        
                self.retranslateUi(Mese)
        
                self.label_ResultsforPeriod.setText("Results for Period ")
    
    def pushButton_EnterallDecisions_was_clicked(self):
        self.Dialog_SelectaCompany = QtWidgets.QDialog()
        self.Dialog_SelectaCompany_ui = Ui_Dialog_EnterallDecisions()
        self.Dialog_SelectaCompany_ui.setupUi(self.Dialog_SelectaCompany)
        self.Dialog_SelectaCompany.exec()
    
    def pushButton_ReviewDecisions_was_clicked(self):
        self.Dialog_SelectaCompany_Review = QtWidgets.QDialog()
        self.Dialog_SelectaCompany_Review_ui = Ui_Dialog_ReviewDecisions()
        self.Dialog_SelectaCompany_Review_ui.setupUi(self.Dialog_SelectaCompany_Review)
        self.Dialog_SelectaCompany_Review.exec()
    
    def pushButton_ClosePeriod_was_clicked(self):
        log_file = open("ClosePeriod_log.txt", "r").readline()
        length = len(log_file.split(" ")) - 1
        if length == 8 or self.period == 0:
            self.Dialog_ClosePeriod = QtWidgets.QDialog()
            self.Dialog_ClosePeriod_ui = Ui_Dialog_ClosePeriod()
            self.Dialog_ClosePeriod_ui.setupUi(self.Dialog_ClosePeriod)
            self.Dialog_ClosePeriod.exec()
            
            
            
        else:     
            self.Dialog_ClosePeriod_Error = QtWidgets.QDialog()
            self.Dialog_ClosePeriod_Error_ui = Ui_Dialog_ClosePeriod_Error()
            self.Dialog_ClosePeriod_Error_ui.setupUi(self.Dialog_ClosePeriod_Error)
            self.Dialog_ClosePeriod_Error.exec()
        #check
        check_file = open("result.txt", "r").readline()
        
        if check_file == "":
            self.period = 0
            
        else:   
            self.period = literal_eval(check_file)["now_tick"]
            self.pushButton_EnterallDecisions.setEnabled(True)
            self.pushButton_ReviewDecisions.setEnabled(True)
            self.pushButton_View.setEnabled(True)
            self.pushButton_Graph.setEnabled(True)
            self.pushButton_Print.setEnabled(True)
         
        self.retranslateUi(Mese)
    #def pushButton_SelectPeriod_was_clicked(self):
        #pass
    
    def pushButton_View_was_clicked(self):
        pass
    
    def pushButton_Graph_was_clicked(self):
        pass
    
    def pushButton_Print_was_clicked(self):
        self.Dialog_Print = QtWidgets.QDialog()
        self.Dialog_Print_ui = Ui_Dialog_Print()
        self.Dialog_Print_ui.setupUi(self.Dialog_Print)
        self.Dialog_Print.exec()
    
    def pushButton_SetParameters_was_clicked(self):
        self.Dialog_setParameters = QtWidgets.QDialog()
        self.Dialog_setParameters_ui = Ui_Dialog_setParameters()
        self.Dialog_setParameters_ui.setupUi(self.Dialog_setParameters)
        self.Dialog_setParameters.exec()
    
    def pushButton_ChangeLevelOfPlay_was_clicked(self):
        self.Dialog_Change_Level_of_Play = QtWidgets.QDialog()
        self.Dialog_Change_Level_of_Play_ui = Ui_Dialog_Change_Level_of_Play()
        self.Dialog_Change_Level_of_Play_ui.setupUi(self.Dialog_Change_Level_of_Play)
        self.Dialog_Change_Level_of_Play.exec()
    
    def actionEnglish_was_clicked(self, s):
        if s == True:
            self.action_Rus.setChecked(False)
    
    def action_Rus_was_clicked(self, s):
        if s == True:
            self.actionEnglish.setChecked(False)
    
    def actionDark_was_clicked(self):
        pass
    
    def actionLight_was_clicked(self):
        pass
    
    def actionContact_us_was_clicked(self):
        self.Dialog_Contactus = QtWidgets.QDialog()
        self.Dialog_Contactus_ui = Ui_Dialog_Contactus()
        self.Dialog_Contactus_ui.setupUi(self.Dialog_Contactus)
        self.Dialog_Contactus.exec()




app = QtWidgets.QApplication([])
Mese = QtWidgets.QMainWindow()
ui = Ui_Mese()
ui.setupUi(Mese)
Mese.show()
app.exec()

