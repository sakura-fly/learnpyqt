"""
显示鼠标的坐标
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        # xy显示在QLabel组件
        self.text = "x: %d,  y: %d" % (x, y)
        self.lable = QLabel(self.text, self)
        grid.addWidget(self.lable, 0, 0, Qt.AlignTop)

        # 鼠标追踪默认没开，当有点击事件时才会开启
        self.setMouseTracking(True)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    # e是事件对象。里面有我们出发的事件（移动鼠标）
    # x(),y()方法得到鼠标坐标，拼成字符串输出到QLabel组件
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        self.lable.setText("x:%d,y:%d" % (x, y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
