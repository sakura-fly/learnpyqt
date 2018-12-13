import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QApplication


class Exmaple(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        menuBar = self.menuBar()
        fileNume = menuBar.addMenu("文件")

        # 创建一个新菜单
        impMenu = QMenu("import", self)
        # addAction添加动作
        impAct = QAction("import mail", self)
        impMenu.addAction(impAct)

        #  新建一个
        newAct = QAction("new", self)

        # 添加到file菜单
        fileNume.addAction(newAct)
        fileNume.addMenu(impMenu)

        self.resize(600, 600)
        self.setWindowTitle("子菜单")
        self.show()


app = QApplication(sys.argv)
ex = Exmaple()
sys.exit(app.exec_())
