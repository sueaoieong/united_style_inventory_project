import sys,us_main
from search_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication

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
            sql="Select * from "
        elif category=="post ID":
            sql="Select * from "

    def change_table(self):
        category=self.ui.comboBox.currentText()
        if category=="Barcode":
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Barcode","貨名","顏色","尺寸","庫存"])

        elif category=="post ID":
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["post ID","貨名","顏色","尺寸","日期"])

if __name__=="__main__":
    app = QApplication(sys.argv)
    w=search_show()
    sys.exit(app.exec_())
