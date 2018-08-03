import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

class out_log_ui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("出倉記錄")
        self.addContent()
        self.show()

    def addContent(self):
        label1=QLabel("交收人名:",self)
        people_text=QLineEdit(self)
        label2=QLabel("Barcode:",self)
        barcode_text=QLineEdit(self)

        label1.move(20,50)
        people_text.move(100,50)
        label2.move(20,70)
        barcode_text.move(100,70)

if __name__=="__main__":
    app=QApplication(sys.argv)
    a=out_log_ui()
    sys.exit(app.exec_())
