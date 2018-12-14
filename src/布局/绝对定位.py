"""
程序指定了组件的位置并且每个组件的大小用像素作为单位来丈量。当你使用了绝对定位，我们需要知道下面的几点限制：

如果我们改变了窗口大小，组件的位置和大小并不会发生改变。
在不同平台上，应用的外观可能不同
改变我们应用中的字体的话可能会把应用弄得一团糟。
如果我们决定改变我们的布局，我们必须完全重写我们的布局，这样非常乏味和浪费时间。

"""
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lable1 = QLabel("111", self)
        lable1.move(15, 10)

        lable2 = QLabel("222", self)
        lable2.move(35, 40)

        lable3 = QLabel("333", self)
        lable3.move(55, 70)

        self.resize(250, 150)
        self.setWindowTitle("绝对定位")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
