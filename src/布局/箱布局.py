"""
布局管理器的布局管理类非常灵活，实用。它是将组件定位在窗口上的首选方式。QHBoxLayout和QVBoxLayout是两个基础布局管理类，他们水平或垂直的线性排列组件。想象一下我们需要在右下角排列两个按钮。为了使用箱布局，我们将使用一个水平箱布局和垂直箱布局来实现。同样为了使用一些必要的空白，我们将添加一些拉伸因子。
"""
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建俩按钮
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # 创建一个水平布局增加一个拉伸因子和两个按钮
        # 拉伸因子在两个按钮之间增加一个可伸缩的空间
        # 这会将按钮推到右边
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了创建必要的布局，吧水兵布局放在数值布局内、
        # 拉伸因子将包含两个按钮的水平布局推到底部
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置窗口的主布局
        self.setLayout(vbox)

        self.resize(600, 600)
        self.setWindowTitle("箱布局")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
