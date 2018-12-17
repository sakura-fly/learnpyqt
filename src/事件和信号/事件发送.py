"""
有时候我们会想知道是哪个组件发出了一个信号，PyQt5里的sender()方法能搞定这件事。
这个例子里有俩按钮，btnClicked()方法决定了是哪个按钮能调用sender()方法。
"""
import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("b1", self)
        btn2 = QPushButton("b2", self)

        btn1.move(30, 50)
        btn2.move(130, 50)

        # 俩按钮都邦洞用一个slot
        btn1.clicked.connect(self.btnClicked)
        btn2.clicked.connect(self.btnClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('事件发送')
        self.show()

    # sender()方法的方式决定了事件源。状态栏显示了被电击的按钮
    def btnClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was press")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
