import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 实例化QGridLayout类，并设为窗口的布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 这是之后按钮的内容
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 创建网格的定位表
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 创建按钮，并添加到布局
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        # self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
