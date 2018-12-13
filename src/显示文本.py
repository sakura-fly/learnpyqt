from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QToolTip
from future.moves import sys


class Exmaple(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):

        # 字体，10px的SansSerif
        QToolTip.setFont(QFont('SansSerif', 10))

        # 设置提示，可以使用富文本格式
        self.setToolTip("This is a <b>QWidget</b> widget")


        btn = QPushButton("Button", self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("hello word")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Exmaple()
    sys.exit(app.exec_())
