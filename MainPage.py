from PyQt5.QtWidgets import *
from qt_kods.MainPage_python import *
from addTheBook import addPage
from DeleteWindow import deletePage
from ShowWindow import showPage



class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")


        self.ui.Add_Book.clicked.connect(self.open_Add_Book)
        self.ui.Remove_book.clicked.connect(self.open_Remove_Book)
        self.ui.Show_book.clicked.connect(self.open_Show_Book)

        self.ShowWindow=showPage()
        self.addTheBook=addPage()
        self.deleteTheBook=deletePage()


    def open_Add_Book(self):
        self.addTheBook.setFixedSize(self.addTheBook.size())
        self.addTheBook.show()
        self.deleteTheBook.hide()
        self.ShowWindow.hide()

    def open_Show_Book(self):
        self.ShowWindow.setFixedSize(self.ShowWindow.size())
        self.ShowWindow.listBook()
        self.ShowWindow.show()
        self.addTheBook.hide()
        self.deleteTheBook.hide()

    def open_Remove_Book(self):
        self.deleteTheBook.setFixedSize(self.deleteTheBook.size())
        self.deleteTheBook.listBook()
        self.deleteTheBook.show()
        self.addTheBook.hide()
        self.ShowWindow.hide()

app = QApplication([])
window =main()
window.setFixedSize(window.size())
window.show()
app.exec_()
