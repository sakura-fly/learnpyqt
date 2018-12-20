import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton("dialog", self)
        self.btn.move(20, 10)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.resize(300, 300)
        self.setWindowTitle("dialog")
        self.show()

    def showDialog(self):
        # 第一个字符串是标题，第二个是提示文本
        # 返回一个文本内容和布尔，点击了ok是true，否则false
        text, ok = QInputDialog.getText(self,"input dialog", "enter name")

        # 收到之显示内容
        if ok:
            self.le.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
