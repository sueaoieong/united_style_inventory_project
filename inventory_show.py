import sys
from inventory_ui import Ui_Form
from PyQt5.QtWidgets import QDialog,QApplication

class inventory_show(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    w=inventory_show()
    sys.exit(app.exec_())
