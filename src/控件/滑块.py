import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSlider, QApplication


class Test(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged[int].connect(self.change)
        self.show()

    def change(self, value):
        print(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
