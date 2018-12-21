import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication

app = QApplication(sys.argv)

label = QLabel("666")
label.setGeometry(300, 300, 300, 300)

# 设置为闪屏模式，没框
label.setWindowFlags(Qt.SplashScreen)
label.show()

sys.exit(app.exec_())
