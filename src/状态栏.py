import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("666")

        self.resize(300, 300)
        self.setWindowTitle("statusBar")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())