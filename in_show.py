import sys
from in_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem

class in_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.table_create()
        self.ui.pushButton.clicked.connect(self.get_info)
        self.show()

    def table_create(self):
        #rowposition=self.ui.tableWidget.rowCount()
        #self.ui.tableWidget.insertRow(rowposition)
        self.ui.tableWidget.setRowCount(10)
        self.ui.tableWidget.setColumnCount(10)
        #self.ui.tableWidget.setItem(0,0,QTableWidgetItem("ad"))
        #self.ui.tableWidget.setItem(0,1,QTableWidgetItem("ad"))
        #self.ui.tableWidget.setItem(0,2,QTableWidgetItem("ad"))

    def get_info(self):
        id=self.ui.lineEdit.text()
        print(id)
        self.ui.tableWidget.setItem(0,0,QTableWidgetItem(id))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w=in_show()
    sys.exit(app.exec_())
