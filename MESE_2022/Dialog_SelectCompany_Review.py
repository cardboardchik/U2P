
## by karton4ik

from PyQt6 import QtCore, QtGui, QtWidgets
from Dialog_EnterDecisions import Ui_Dialog
from ast import literal_eval


class Ui_Dialog_ReviewDecisions(object):
    def setupUi(self, Dialog_ReviewDecisions):
        Dialog_ReviewDecisions.setObjectName("Dialog_ReviewDecisions")
        Dialog_ReviewDecisions.resize(200, 300)
        Dialog_ReviewDecisions.setMinimumSize(QtCore.QSize(200, 300))
        Dialog_ReviewDecisions.setMaximumSize(QtCore.QSize(200, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_ReviewDecisions.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_ReviewDecisions)
        self.buttonBox.setGeometry(QtCore.QRect(17, 260, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QtWidgets.QListWidget(Dialog_ReviewDecisions)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 180, 240))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setMovement(QtWidgets.QListView.Movement.Static)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        
        self.file = literal_eval(open("Dialog_Setup.txt", "r").readline())
        
        for i in range(len(self.file)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
        
        
        self.listWidget.itemDoubleClicked.connect(self.listWidget_was_doubleClicked)
        self.retranslateUi(Dialog_ReviewDecisions)
        self.buttonBox.accepted.connect(Dialog_ReviewDecisions.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_ReviewDecisions.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_ReviewDecisions)

    def retranslateUi(self, Dialog_ReviewDecisions):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ReviewDecisions.setWindowTitle(_translate("Dialog_ReviewDecisions", "Select a Company"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        for i in range(1, len(self.file) + 1):
            try:
                item = self.listWidget.item(i-1)
                item.setText(_translate("Dialog_EnterallDecisions", self.file[f"Company_{i}"]))
                
            except KeyError:
                pass
        
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def listWidget_was_doubleClicked(self, lstitem):
        self.f = open("logs.txt", "w")
        self.f.write(lstitem.text()+"\n"+ str(self.listWidget.currentRow()))
        
        self.f.close()
        self.Dialog_EnterDecisions = QtWidgets.QDialog()
        self.Dialog_EnterDecisions_ui = Ui_Dialog()
        self.Dialog_EnterDecisions_ui.setupUi(self.Dialog_EnterDecisions)
        self.Dialog_EnterDecisions.exec()
        
        
            
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ReviewDecisions = QtWidgets.QDialog()
    ui = Ui_Dialog_ReviewDecisions()
    ui.setupUi(Dialog_ReviewDecisions)
    Dialog_ReviewDecisions.show()
    sys.exit(app.exec())
