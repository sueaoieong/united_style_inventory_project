import sys,us_main,datetime
from out_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMessageBox

class out_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.db=us_main.us_main()
        self.fetch_people()
        self.table_create()
        self.ui.lineEdit_2.editingFinished.connect(self.get_info)
        self.ui.pushButton.setAutoDefault(False)
        self.ui.pushButton.clicked.connect(self.save_data)
        self.show()


    def fetch_people(self):
        sql="SELECT 人名 from people"
        result=self.db.search_all(self.db.conn,sql)
        for i in result:
            temp=i[0]
            print(temp)
            self.ui.comboBox.addItem(temp)

    def table_create(self):
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Barcode","貨名","顏色","尺寸"])

    def save_data(self):
        date=datetime.datetime.today().strftime("%Y-%m-%d")
        name=self.ui.comboBox.currentText()
        print(name)
        totalrow=self.ui.tableWidget.rowCount()
        print(totalrow)
        if totalrow!=0:
            for i in range(totalrow):
                barcode=self.ui.tableWidget.item(i,0).text()
                sql="INSERT INTO out_DB(交收人員, Barcode, 日期) VALUES (?,?,?)"
                value=(name,barcode,date)
                self.db.add_item(self.db.conn,sql,value)
            print(totalrow)
            for i in range(totalrow):
                self.ui.tableWidget.removeRow(0)

            msg=QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("儲存完成!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def get_info(self):
        barcode=self.ui.lineEdit_2.text()
        if barcode=="":
            pass
        else:
            sql="SELECT 貨名,顏色,尺寸 FROM inventory where Barcode=?"
            temp=self.db.search_item(self.db.conn,sql,(barcode,))
            name=temp[0]
            color=temp[1]
            size=temp[2]
            row=self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row,0,QTableWidgetItem(barcode))
            self.ui.tableWidget.setItem(row,1,QTableWidgetItem(name))
            self.ui.tableWidget.setItem(row,2,QTableWidgetItem(color))
            self.ui.tableWidget.setItem(row,3,QTableWidgetItem(size))

            self.ui.lineEdit_2.clear()



if __name__=="__main__":
    app = QApplication(sys.argv)
    w=out_show()
    sys.exit(app.exec_())
