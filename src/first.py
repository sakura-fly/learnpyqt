import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 穿件一个应用对象application,sys.argv是一个来自命令行的参数列表，Python脚本可以运行在shell，这是我们控制启动的一种方式
    app = QApplication(sys.argv)
    # QWidget组件是pyqt住所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。默认的构造方法没有父类。没有父类的widget组件将被作为窗口使用
    w = QWidget()
    # 调整了大小
    w.resize(250, 150)
    # 移动到(300,300) 默认屏幕中间
    w.move(300, 300)
    # 标题，显示在标题栏
    w.setWindowTitle('Simple')
    w.setWindowIcon(QIcon('rin.png'))
    # 显示widget，一个widget对象被创建，并显示在屏幕
    w.show()
    # 最后，应用进入主循环。
    # 在这个地方，事件处理开始执行。
    # 主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理。
    # 如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
    # exec_()方法有一个下划线。因为exec是Python保留关键字。因此，用exec_()来代替。
    sys.exit(app.exec_())
