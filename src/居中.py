from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from future.moves import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle("center")
        self.show()

    def center(self):

        # 获得主窗口的一个矩形特定集合图形，包含了窗口的框架
        qr = self.frameGeometry()
        # 算出相对于显示器的绝对值。
        # 从这个绝对值中我们获得了屏幕的中心的
        cp = QDesktopWidget().availableGeometry().center()
        # 设置了宽高，把矩形的忠心放到屏幕中间。矩形大小不变
        qr.moveCenter(cp)
        # 移动窗口的左上方到qr矩形左上方的点，因此居中在屏幕
        self.move(qr.topLeft())


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
