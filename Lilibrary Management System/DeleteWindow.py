from PyQt5.QtWidgets import *
from qt_kods.DeleteWindow_python import Ui_DeleteWindow

class deletePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.delwindow = Ui_DeleteWindow()
        self.delwindow.setupUi(self)

        self.delwindow.deleteMnRt.clicked.connect(self.close_window)

        self.delwindow.finalDeleteButton.clicked.connect(self.delete_from_label)
        self.delwindow.finalDeleteButton.clicked.connect(self.clearLabel)
    def delete_from_label(self):
        # Label'da yazılan metni al
        title_to_delete =self.delwindow.deleteName.text()
        if title_to_delete:  # Eğer bir metin varsa
            found = False
            for row in range(self.delwindow.tableWidget.rowCount()):
                if self.delwindow.tableWidget.item(row, 0).text() == title_to_delete:  # Başlık eşleşirse
                    found = True
                    self.delwindow.tableWidget.removeRow(row)  # Table Widget'tan satırı sil

                    # Txt dosyasını güncelle
                    with open("books.txt", "r+") as f:
                        lines = f.readlines()
                        f.seek(0)
                        for line in lines:
                            if not line.startswith(title_to_delete):  # Başlık eşleşmiyorsa
                                f.write(line)
                        f.truncate()
                    break

            if not found:
                QMessageBox.warning(self, "WARNING", "The title you entered was not found.")
        else:
            QMessageBox.warning(self, "WARNING", "Please enter a title.")


    def listBook(self):
        with open("books.txt", "r") as f:
            data = [line.strip().split(",") for line in f.readlines()]

        for row_num, row_data in enumerate(data):
            self.delwindow.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.delwindow.tableWidget.setItem(row_num, col_num, QTableWidgetItem(col_data))

    def close_window(self):
        self.delwindow.tableWidget.clearContents()
        self.delwindow.tableWidget.setRowCount(0)
        self.hide()

    def clearLabel(self):
        self.delwindow.deleteName.clear()