# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteWindow(object):
    def setupUi(self, DeleteWindow):
        DeleteWindow.setObjectName("DeleteWindow")
        DeleteWindow.resize(700, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteWindow.setWindowIcon(icon)
        DeleteWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/arkaplan/duvar-resimleri-kutuphane-kitap-raf-arka-plan-vektor.jpg.jpg);}")
        self.centralwidget = QtWidgets.QWidget(DeleteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 20, 550, 450))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 500, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.deleteName = QtWidgets.QLineEdit(self.centralwidget)
        self.deleteName.setGeometry(QtCore.QRect(100, 550, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deleteName.setFont(font)
        self.deleteName.setObjectName("deleteName")
        self.finalDeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.finalDeleteButton.setGeometry(QtCore.QRect(340, 480, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.finalDeleteButton.setFont(font)
        self.finalDeleteButton.setObjectName("finalDeleteButton")
        self.deleteMnRt = QtWidgets.QPushButton(self.centralwidget)
        self.deleteMnRt.setGeometry(QtCore.QRect(340, 570, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deleteMnRt.setFont(font)
        self.deleteMnRt.setObjectName("deleteMnRt")
        DeleteWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DeleteWindow)
        self.statusbar.setObjectName("statusbar")
        DeleteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DeleteWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteWindow)

    def retranslateUi(self, DeleteWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteWindow.setWindowTitle(_translate("DeleteWindow", "DeleteWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DeleteWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DeleteWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DeleteWindow", "Release"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DeleteWindow", "Page"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("DeleteWindow", "Enter THe Book Name"))
        self.deleteName.setPlaceholderText(_translate("DeleteWindow", "Exp. Atik Ali"))
        self.finalDeleteButton.setText(_translate("DeleteWindow", "Remove "))
        self.deleteMnRt.setText(_translate("DeleteWindow", "Return Main Page"))
from icons import arkaplan_rc
from icons import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteWindow = QtWidgets.QMainWindow()
    ui = Ui_DeleteWindow()
    ui.setupUi(DeleteWindow)
    DeleteWindow.show()
    sys.exit(app.exec_())
