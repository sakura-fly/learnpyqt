"""
在网格中，组件可以跨多列或多行。在这个例子中，我们对它进行一下说明。
"""
import sys

from PyQt5.QtWidgets import QLabel, QWidget, QTextEdit, QLineEdit, QGridLayout, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # 创建个布局，设置组件之间的间距
        grid = QGridLayout()
        grid.setSpacing(10)


        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 如果我们想网格增加一个组件，我们可以提供组件的跨行和跨列参数
        # 我们在这里垮了5行
        grid.addWidget(reviewEdit, 3, 1)

        self.setLayout(grid)

        # self.resize(600, 600)
        self.setWindowTitle('Review')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
