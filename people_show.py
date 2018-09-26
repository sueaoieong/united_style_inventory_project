import sys
from people_ui import Ui_Form
import us_main
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import QtCore

class people_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.db=us_main.us_main()

        self.ui.pushButton.clicked.connect(self.add_data)
        self.ui.pushButton_2.clicked.connect(self.delete_data)
        self.show()

    def add_data(self):
        name=self.ui.lineEdit.text()
        tel=self.ui.lineEdit_2.text()
        sql="INSERT INTO people(人名,電話)VALUES(?,?)"
        value=(name,tel)
        self.db.add_item(self.db.conn,sql,value)

    def delete_data(self):
        name=self.ui.lineEdit.text()
        tel=self.ui.lineEdit_2.text()
        if name!="":
            sql="DELETE FROM people where 人名=?"
            value=(name,)
        else:
            sql="DELETE FROM people where 電話=?"
            value=(tel,)
        self.db.delete_item(self.db.conn,sql,value)

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    w=people_show()
    sys.exit(app.exec_())
