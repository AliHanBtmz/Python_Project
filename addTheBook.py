from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from qt_kods.addTheBook_python import Ui_AddWindow
from PyQt5.QtCore import Qt



class addPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.addwindow = Ui_AddWindow()
        self.addwindow.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.addwindow.addMnRt.clicked.connect(self.close_window)
        self.addwindow.bookRelaseLine.setValidator(QIntValidator(0, 2025, self))
        self.addwindow.pageNumberLine.setValidator(QIntValidator(0, 10000, self))
        self.addwindow.finalAddBookButton.clicked.connect(self.write_final)
        self.addwindow.finalAddBookButton.clicked.connect(self.clearLine)

    def write_final(self):
        title = self.addwindow.bookNameLine.text()
        author = self.addwindow.bookAuthorLine.text()
        release = self.addwindow.bookRelaseLine.text()
        num_pages = self.addwindow.pageNumberLine.text()

        if title and author and release and num_pages:
            # Dosyanın var olup olmadığını kontrol et
            with open("books.txt", "r") as f:
                existing_data = f.read()
                if f"{title},{author},{release},{num_pages}" in existing_data:
                    QMessageBox.warning(self, "WARNING", "This book is already registered.")
                else:

                    with open("books.txt", "a") as f:
                        f.write(f"{title},{author},{release},{num_pages}\n")
                    QMessageBox.information(self, "SUCCESS", "Book information has been successfully saved.")
        else:
            QMessageBox.warning(self, "WARNING", "Please enter all information.")


    def clearLine(self):
        self.addwindow.bookNameLine.clear()
        self.addwindow.pageNumberLine.clear()
        self.addwindow.bookRelaseLine.clear()
        self.addwindow.bookAuthorLine.clear()
    def close_window(self):
        self.hide()

