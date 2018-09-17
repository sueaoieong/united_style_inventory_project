import sys,us_main
from search_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem

class search_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.db=us_main.us_main()
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Barcode","貨名","顏色","尺寸","庫存"])
        self.ui.comboBox.currentIndexChanged.connect(self.change_table)
        self.ui.pushButton.clicked.connect(self.get_info)
        self.show()

    def get_info(self):
        category=self.ui.comboBox.currentText()
        value=self.ui.lineEdit.text()
        print(category,value)
        if category=="Barcode":
            sql="SELECT * from goods_amount where Barcode = ?"
            temp=self.db.search_item(self.db.conn,sql,(value,))
            print("=====Barcode checking=====")
            print(temp)
            sql1="SELECT 貨名,顏色,尺寸 from inventory where Barcode = ?"
            temp2=self.db.search_item(self.db.conn,sql1,(value,))
            if temp==None:
                pass
            else:
                row=self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row,0,QTableWidgetItem(temp[0]))
                self.ui.tableWidget.setItem(row,1,QTableWidgetItem(temp2[0]))
                self.ui.tableWidget.setItem(row,2,QTableWidgetItem(temp2[1]))
                self.ui.tableWidget.setItem(row,3,QTableWidgetItem(temp2[2]))
                self.ui.tableWidget.setItem(row,4,QTableWidgetItem(str(temp[1])))
        elif category=="post ID":
            sql="SELECT post_ID,貨名,顏色,尺寸,link,Barcode,日期 from inventory where post_ID=?"
            temp=self.db.search_items(self.db.conn,sql,(value,))

            print("====post id checking=====")
            print(temp)
            if temp==None:
                pass
            else:
                for i in temp:
                    print(i)
                    row=self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row)
                    self.ui.tableWidget.setItem(row,0,QTableWidgetItem(i[0]))
                    self.ui.tableWidget.setItem(row,1,QTableWidgetItem(i[1]))
                    self.ui.tableWidget.setItem(row,2,QTableWidgetItem(i[2]))
                    self.ui.tableWidget.setItem(row,3,QTableWidgetItem(i[3]))
                    self.ui.tableWidget.setItem(row,4,QTableWidgetItem(i[4]))
                    self.ui.tableWidget.setItem(row,5,QTableWidgetItem(i[5]))
                    self.ui.tableWidget.setItem(row,6,QTableWidgetItem(i[6]))


    def change_table(self):
        category=self.ui.comboBox.currentText()
        if category=="Barcode":
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Barcode","貨名","顏色","尺寸","庫存"])
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

        elif category=="post ID":
            self.ui.tableWidget.setColumnCount(7)
            self.ui.tableWidget.setHorizontalHeaderLabels(["post ID","貨名","顏色","尺寸","link","Barcode","日期"])
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w=search_show()
    sys.exit(app.exec_())
