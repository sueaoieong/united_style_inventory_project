import sys
from main_ui import Ui_Form
import in_show,out_show,people_show,search_show,inventory_show
from PyQt5.QtWidgets import QDialog,QApplication

class main_show(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.callInUI)
        self.ui.pushButton_7.clicked.connect(self.callOutUI)
        self.ui.pushButton_3.clicked.connect(self.callInventoryUI)
        self.ui.pushButton_4.clicked.connect(self.callPeopleUI)
        self.ui.pushButton_2.clicked.connect(self.callSearchUI)
        self.show()

    def callInUI(self):
        self.test=in_show.in_show()

    def callOutUI(self):
        self.test=out_show.out_show()

    def callInventoryUI(self):
        self.test=inventory_show.inventory_show()

    def callSearchUI(self):
        self.test=search_show.search_show()

    def callPeopleUI(self):
        self.test=people_show.people_show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w=main_show()
    sys.exit(app.exec_())
