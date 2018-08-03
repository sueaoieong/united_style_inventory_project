import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

class people_ui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("交收人員名單")
        self.addContent()
        self.show()

    def addContent(self):
        label1=QLabel("交收人名:",self)
        people_text=QLineEdit(self)
        but1=QPushButton("add",self)

        label1.move(20,50)
        people_text.move(100,50)
        but1.move(400,50)


if __name__=="__main__":
    app=QApplication(sys.argv)
    a=people_ui()
    sys.exit(app.exec_())
