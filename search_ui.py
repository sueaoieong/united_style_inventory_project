import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox

class search_ui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("查詢")
        self.addContent()
        self.show()

    def addContent(self):
        cat_box=QComboBox(self)
        search_text=QLineEdit(self)
        cat_box.addItem("post_ID")
        cat_box.addItem("類型")
        cat_box.addItem("Barcode")
        cat_box.addItem("貨名")


        cat_box.move(20,50)
        search_text.move(100,50)


if __name__=="__main__":
    app=QApplication(sys.argv)
    a=search_ui()
    sys.exit(app.exec_())
