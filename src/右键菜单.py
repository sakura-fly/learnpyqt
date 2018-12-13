import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        self.setWindowTitle("右键菜单")
        self.show()

    # 实现菜单
    def contextMenuEvent(self, QContextMenuEvent):
        # 在这还可以干一些别的事情


        # 新建一个菜单
        cmenu = QMenu(self)

        # 子菜单
        newNume = QMenu("new", self)
        newNume.addAction("file")
        cmenu.addMenu(newNume)

        # 两个动作
        QuitAct = cmenu.addAction("quit")
        openAct = cmenu.addAction("open")

        # exec_()方法显示菜单
        # 从鼠标右键时间对象中获得当前坐标
        # mapToGlobal()方法把当前相对坐标转换为窗口的绝对坐标

        # exec_()不穿参数菜单在左上角，接收的坐标按绝对坐标处理
        # QContextMenuEvent.pos()获取鼠标相对于APP的坐标
        # 不转换坐标菜单以相对坐标为绝对坐标的位置显示
        # mapToGlobal()方法把当前相对坐标转换为窗口的绝对坐标
        # 菜单出现在鼠标位置
        action = cmenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))

        # 触发事件，关闭程序
        if action == QuitAct:
            QApplication.quit()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
