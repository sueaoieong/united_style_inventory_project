import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont
import in_log_ui,out_log_ui,search_ui,people_ui

class WareHouseapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setGeometry(500,300,350,350)
        self.setWindowTitle("United Style倉存記錄")
        self.addButton()
        self.show()

    def addButton(self):
        newfont = QFont("Times", 24, QFont.Bold)
        label1=QLabel("Welcome!",self)
        label1.setFont(newfont)
        in_button=QPushButton("存倉", self)
        out_button=QPushButton("出倉", self)
        search_button=QPushButton("查詢", self)
        people_button=QPushButton("交收人員", self)

        label1.move(10,10)
        in_button.move(50,100)
        in_button.clicked.connect(self.callInLog)
        out_button.move(200,100)
        out_button.clicked.connect(self.callOutLog)
        search_button.move(50,200)
        search_button.clicked.connect(self.callSearch)
        people_button.move(200,200)
        people_button.clicked.connect(self.callPeople)

    def callInLog(self):
        self.test=in_log_ui.in_log_ui()


    def callOutLog(self):
        self.test=out_log_ui.out_log_ui()

    def callSearch(self):
        self.test=search_ui.search_ui()

    def callPeople(self):
        self.test=people_ui.people_ui()

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=WareHouseapp()

    sys.exit(app.exec_())
