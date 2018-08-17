import sys,us_main
from in_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem

class in_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.db=us_main.us_main()
        self.ui.setupUi(self)
        self.table_create()
        self.ui.pushButton.clicked.connect(self.get_info)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.show()

    def save_data(self):
        pass
    def table_create(self):
        #rowposition=self.ui.tableWidget.rowCount()
        #self.ui.tableWidget.insertRow(rowposition)

        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["post ID","貨名","顏色","尺寸","庫存"])
        #self.ui.tableWidget.setItem(0,0,QTableWidgetItem("ad"))
        #self.ui.tableWidget.setItem(0,1,QTableWidgetItem("ad"))
        #self.ui.tableWidget.setItem(0,2,QTableWidgetItem("ad"))

    def get_info(self):
        id=self.ui.lineEdit.text()
        sql="SELECT 貨名 FROM goods where post_ID=?"

        temp=self.db.search_item(self.db.conn,sql,(id,))
        print(type(temp),temp)
        print(temp[0])
        name=temp[0]
        color=self.ui.lineEdit_2.text()
        size=self.ui.lineEdit_3.text()
        qty=self.ui.lineEdit_4.text()

        row=self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row,0,QTableWidgetItem(id))
        self.ui.tableWidget.setItem(row,1,QTableWidgetItem(name))
        self.ui.tableWidget.setItem(row,2,QTableWidgetItem(color))
        self.ui.tableWidget.setItem(row,3,QTableWidgetItem(size))
        self.ui.tableWidget.setItem(row,4,QTableWidgetItem(qty))


if __name__=="__main__":
    app = QApplication(sys.argv)
    w=in_show()
    sys.exit(app.exec_())
