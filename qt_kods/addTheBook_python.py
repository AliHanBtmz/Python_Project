# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTheBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(700, 708)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddWindow.setWindowIcon(icon)
        AddWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/arkaplan/duvar-resimleri-kutuphane-kitap-raf-arka-plan-vektor.jpg.jpg);}\n"
"\n"
"#verticalLayout_2{\n"
"background-color: rgb(255, 255, 255);}")
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.finalAddBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.finalAddBookButton.setGeometry(QtCore.QRect(130, 430, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.finalAddBookButton.setFont(font)
        self.finalAddBookButton.setObjectName("finalAddBookButton")
        self.addMnRt = QtWidgets.QPushButton(self.centralwidget)
        self.addMnRt.setGeometry(QtCore.QRect(420, 430, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addMnRt.setFont(font)
        self.addMnRt.setObjectName("addMnRt")
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setGeometry(QtCore.QRect(50, 75, 591, 241))
        self.verticalWidget_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.bookNameLine = QtWidgets.QLineEdit(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookNameLine.sizePolicy().hasHeightForWidth())
        self.bookNameLine.setSizePolicy(sizePolicy)
        self.bookNameLine.setToolTip("")
        self.bookNameLine.setStatusTip("")
        self.bookNameLine.setAccessibleName("")
        self.bookNameLine.setAccessibleDescription("")
        self.bookNameLine.setAutoFillBackground(False)
        self.bookNameLine.setInputMask("")
        self.bookNameLine.setText("")
        self.bookNameLine.setClearButtonEnabled(True)
        self.bookNameLine.setObjectName("bookNameLine")
        self.verticalLayout_2.addWidget(self.bookNameLine)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.bookAuthorLine = QtWidgets.QLineEdit(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookAuthorLine.sizePolicy().hasHeightForWidth())
        self.bookAuthorLine.setSizePolicy(sizePolicy)
        self.bookAuthorLine.setInputMask("")
        self.bookAuthorLine.setText("")
        self.bookAuthorLine.setFrame(True)
        self.bookAuthorLine.setReadOnly(False)
        self.bookAuthorLine.setClearButtonEnabled(True)
        self.bookAuthorLine.setObjectName("bookAuthorLine")
        self.verticalLayout_2.addWidget(self.bookAuthorLine)
        self.label_4 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.bookRelaseLine = QtWidgets.QLineEdit(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookRelaseLine.sizePolicy().hasHeightForWidth())
        self.bookRelaseLine.setSizePolicy(sizePolicy)
        self.bookRelaseLine.setAutoFillBackground(False)
        self.bookRelaseLine.setText("")
        self.bookRelaseLine.setClearButtonEnabled(True)
        self.bookRelaseLine.setObjectName("bookRelaseLine")
        self.verticalLayout_2.addWidget(self.bookRelaseLine)
        self.label_5 = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.pageNumberLine = QtWidgets.QLineEdit(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageNumberLine.sizePolicy().hasHeightForWidth())
        self.pageNumberLine.setSizePolicy(sizePolicy)
        self.pageNumberLine.setText("")
        self.pageNumberLine.setClearButtonEnabled(True)
        self.pageNumberLine.setObjectName("pageNumberLine")
        self.verticalLayout_2.addWidget(self.pageNumberLine)
        AddWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "ADD THE BOOK"))
        self.finalAddBookButton.setText(_translate("AddWindow", "Add Book"))
        self.addMnRt.setText(_translate("AddWindow", "Return Main Page"))
        self.label_2.setText(_translate("AddWindow", "The Name Of The Book"))
        self.bookNameLine.setPlaceholderText(_translate("AddWindow", "Exp. Çocukluk"))
        self.label_3.setText(_translate("AddWindow", "The Author Of The Book"))
        self.bookAuthorLine.setPlaceholderText(_translate("AddWindow", "Exp. Lev Tolstoy"))
        self.label_4.setText(_translate("AddWindow", "First Release Year"))
        self.bookRelaseLine.setPlaceholderText(_translate("AddWindow", "Exp. 2015"))
        self.label_5.setText(_translate("AddWindow", "Number Of Pages"))
        self.pageNumberLine.setPlaceholderText(_translate("AddWindow", "Exp. 320"))
from icons import arkaplan_rc
from icons import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddWindow = QtWidgets.QMainWindow()
    ui = Ui_AddWindow()
    ui.setupUi(AddWindow)
    AddWindow.show()
    sys.exit(app.exec_())