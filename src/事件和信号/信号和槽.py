"""
在我们的例子中，我们显示了一个QtGui.QLCDNumber和一个QtGui.QSlider类。我们拖动滑块条的把手，lcd数字会变化。
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        # 在这里我们将滑块的valueChanged信号和lcd数字显示的display槽连接在一起。
        # 我们发送者是一个发送了信号的对象,接受者是一个接受的对象.
        # 槽是对信号做出反应的方法
        sld.valueChanged.connect(lcd.display)

        self.resize(600, 600)
        self.setWindowTitle("Signal & slot")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
