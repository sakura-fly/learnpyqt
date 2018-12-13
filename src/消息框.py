from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from future.moves import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(self.sizeHint())
        self.setWindowTitle("Message box")
        self.show()

    # 关闭一个QWidgetclose，Event类事件将被生成。
    # 要修改组件动作我们需要重新实现事件处理方法
    def closeEvent(self, event):

        # 带有两个按钮的message box，yes和no。
        # 第一个字符串是显示在标题栏。
        # 第二个字符串是对话框显示的文本
        # 第三个参数制定了显示在对话框上的按钮的集合
        # 最后一个参数是默认选中的按钮，这个按钮一开始获得焦点
        # 返回值保存在box中
        box = QMessageBox.question(self, "是否退出", "确定退出？",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.Yes)
        if box == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
