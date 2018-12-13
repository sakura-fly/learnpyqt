"""
菜单栏是GUI应用的常规组成部分。是位于各种菜单中的一组命令操作（Mac OS 对待菜单栏有些不同。为了获得全平台一致的效果，我们可以在代码中加入一行：menubar.setNativeMenuBar(False)）。
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, qApp


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # QAction是一个用于菜单栏，工具栏或自定义快捷键的抽象动作行为
        # 我们创建了一个有指定图标和文本为"Exit"的标签
        # 还未这个动作定义了快捷键
        # 第三行当我们鼠标浮上去就会显示一个状态提示
        exitAction = QAction(QIcon("rin.png"), "推出", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出")

        # 当我们选中动作，一个除法信号会被发射
        # 信号连接到QApplication的quit()方法
        # 这样就关闭了应用
        exitAction.triggered.connect(QApplication.quit)

        self.statusBar()

        # menuBar()创建个菜单栏
        # 我们创建一个file菜单，然后将推出添加到file中
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("文件")
        fileMenu.addAction(exitAction)

        self.resize(600, 600)
        self.setWindowTitle("菜单")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
