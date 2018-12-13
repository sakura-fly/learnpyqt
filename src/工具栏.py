"""
菜单可以集成所有命令，这样我们可以在应用中使用这些被集成的命令。工具栏提供了一个快速访问常用命令的方式。
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon("rin.png"), "退出", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar("退出")
        self.toolbar.addAction(exitAct)

        self.resize(600, 600)
        self.setWindowTitle("工具栏")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
