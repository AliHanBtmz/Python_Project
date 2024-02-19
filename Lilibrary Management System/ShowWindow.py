from PyQt5.QtWidgets import *
from qt_kods.ShowWindow_python import Ui_ShowWindow

class showPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.showWindow = Ui_ShowWindow()
        self.showWindow.setupUi(self)

        self.showWindow.showMnRt.clicked.connect(self.close_window)

    def listBook(self):

        with open("books.txt", "r") as f:
            data = [line.strip().split(",") for line in f.readlines()]

        # Table Widget'e verileri ekleme
        for row_num, row_data in enumerate(data):
            self.showWindow.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.showWindow.tableWidget.setItem(row_num, col_num, QTableWidgetItem(col_data))

    def close_window(self):
         self.hide()
         self.showWindow.tableWidget.clearContents()
         self.showWindow.tableWidget.setRowCount(0)