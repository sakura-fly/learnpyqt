import sys

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.testEdit = QTextEdit()
        self.setCentralWidget(self.testEdit)
        self.statusBar()

        openFile = QAction("open",self)
        openFile.setStatusTip("打开文件")
        openFile.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("文件")
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "选择文件", "/")

        if fname[0]:
            f = open(fname[0], "r")

            with f:
                data = f.read()
                self.testEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
