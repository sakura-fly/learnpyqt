"""
有时候我们会想知道是哪个组件发出了一个信号，PyQt5里的sender()方法能搞定这件事。
"""
from PyQt5.QtWidgets import QMainWindow, QPushButton


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("b1", self)
        btn2 = QPushButton("b2", self)

        btn1.move(30,50)
        btn2.move(130,50)

        btn1.clicked()