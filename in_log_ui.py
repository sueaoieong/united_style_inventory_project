import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox

class in_log_ui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("存倉記錄")
        self.addContent()
        self.show()

    def addContent(self):
        label1=QLabel("post_ID:",self)
        post_text=QLineEdit(self)
        label2=QLabel("類型:",self)
        type_box=QComboBox(self)
        type_box.addItem("袋")
        type_box.addItem("眼鏡")
        label3=QLabel("貨名:",self)
        item_text=QLineEdit(self)
        label4=QLabel("顏色:",self)
        color_text=QLineEdit(self)
        label5=QLabel("尺寸:",self)
        size_text=QLineEdit(self)
        label6=QLabel("庫存:",self)
        qty_text=QLineEdit(self)

        label1.move(20,50)
        post_text.move(100,50)
        label2.move(20,70)
        type_box.move(100,70)
        label3.move(20,90)
        item_text.move(100,90)
        label4.move(280,50)
        color_text.move(320,50)
        label5.move(280,70)
        size_text.move(320,70)
        label6.move(280,90)
        qty_text.move(320,90)

if __name__=="__main__":
    app=QApplication(sys.argv)
    a=in_log_ui()
    sys.exit(app.exec_())
