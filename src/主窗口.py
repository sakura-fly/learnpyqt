import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QMenuBar, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 文本编辑区域，放在中间，沾满了剩余所有区域
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon("rin.png"), "退出", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("退出")
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu("文件")
        fileMenu.addAction(exitAct)

        toolBar = self.addToolBar("exit")
        toolBar.addAction(exitAct)

        self.resize(600,600)
        self.setWindowTitle("主窗口")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())



