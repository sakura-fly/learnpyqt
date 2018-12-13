'''
通过程序关闭窗口，简单的初级信号和槽机制

QPushButton(string text, QWidget parent = None)

text显示在按钮中的内容。parent是显示按钮的组件
一个应用的组件应该是分层的，在这个层次中，大多是都有父类。
没有的是顶级窗口

'''
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from future.moves import sys


class Examole(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮，第一个参数是显示的文本，第二个是父组件。
        qbtn = QPushButton("退出", self)
        # 在pyqt中，事件处理系统有信号&槽机制建立。
        # 如果我们点击了按钮，信号clicked被发送
        # QCoreApplication类包含了主事件循环，他处理和转发所有事件
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        self.resize(300, 300)
        self.setWindowTitle("退出")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Examole()
    sys.exit(app.exec_())
