import sys,us_main,datetime,sqlite3

from inventory_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import QtCore

class inventory_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.db=us_main.us_main()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_info)
        self.ui.pushButton_2.clicked.connect(self.clear_alltext)
        self.show()

    def clear_alltext(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()

    def get_info(self):
        post=self.ui.lineEdit.text()
        type=self.ui.lineEdit_2.text()
        name=self.ui.lineEdit_3.text()
        color=self.ui.lineEdit_4.text()
        size=self.ui.lineEdit_5.text()
        cost=self.ui.lineEdit_6.text()
        price=self.ui.lineEdit_7.text()
        link=self.ui.lineEdit_8.text()
        barcode=post+color+size
        date=datetime.datetime.today().strftime("%Y-%m-%d")
        sql1="INSERT INTO inventory(post_ID,貨名,類型,顏色,尺寸,成本,售價,link,barcode,日期) VALUES (?,?,?,?,?,?,?,?,?,?)"
        value1=(post,name,type,color,size,cost,price,link,barcode,date)
        sql2="INSERT INTO goods(post_ID,貨名) VALUES (?,?)"
        value2=(post,name)
        try:
            self.db.add_item(self.db.conn,sql2,value2)
        except sqlite3.IntegrityError:
            print("the record is exist!")
        try:
            self.db.add_item(self.db.conn,sql1,value1)

        except sqlite3.IntegrityError:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("此記錄已經存在!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            msg=QMessageBox()
            msg.setText("輸入成功!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    w=inventory_show()
    sys.exit(app.exec_())
