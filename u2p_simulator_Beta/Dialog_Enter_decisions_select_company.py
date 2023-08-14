
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Enter_decisions_select_company(object):
    def setupUi(self, Dialog_Enter_decisions_select_company):
        Dialog_Enter_decisions_select_company.setObjectName("Dialog_Enter_decisions_select_company")
        Dialog_Enter_decisions_select_company.resize(300, 420)
        Dialog_Enter_decisions_select_company.setMinimumSize(QtCore.QSize(300, 420))
        Dialog_Enter_decisions_select_company.setMaximumSize(QtCore.QSize(300, 420))
        Dialog_Enter_decisions_select_company.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog_Enter_decisions_select_company)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.label.setStyleSheet("color: #1E1E1E;\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px; /* 92.308% */")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Enter_decisions_select_company)
        self.tableWidget.setGeometry(QtCore.QRect(16, 50, 268, 320))
        self.tableWidget.setStyleSheet("QTableView{\n"
"    font:16pt \"Montserrat ExtraBold\";\n"
"    selection-background-color: rgba(0, 0, 0, 0);\n"
"    color:#1E1E1E;\n"
"\n"
"\n"
"}\n"
"QTableView::item {\n"
"    border-bottom: 1px solid #000;\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_Enter_decisions_select_company)
        self.pushButton_cancel.setGeometry(QtCore.QRect(88, 375, 125, 35))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_cancel.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(239, 0, 9, 1);\n"
"color: rgb(0, 0, 0);\n"
"padding-top: -4px;\n"
"\n"
"font-family: Montserrat ExtraBold;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"line-height: 24px;\n"
"letter-spacing: -1px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius: 5px;\n"
"border: 3px solid rgba(47, 47, 47, 1);\n"
"color: #fff;\n"
"padding-top: -1px;\n"
"background-color:rgba(239, 0, 9, 1);\n"
"padding-top: -4px;\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog_Enter_decisions_select_company)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Enter_decisions_select_company)

    def retranslateUi(self, Dialog_Enter_decisions_select_company):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Enter_decisions_select_company.setWindowTitle(_translate("Dialog_Enter_decisions_select_company", "Dialog"))
        self.label.setText(_translate("Dialog_Enter_decisions_select_company", "Ввод решений"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "AAAAAAAA"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "dsad"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog_Enter_decisions_select_company", "dasasd"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_cancel.setText(_translate("Dialog_Enter_decisions_select_company", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Enter_decisions_select_company = QtWidgets.QDialog()
    ui = Ui_Dialog_Enter_decisions_select_company()
    ui.setupUi(Dialog_Enter_decisions_select_company)
    Dialog_Enter_decisions_select_company.show()
    sys.exit(app.exec())
