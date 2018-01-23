# -*- coding: utf-8 -*-
"""第一个程序
"""
"""
learn from 
http://bbs.fishc.com/forum.php?mod=viewthread&tid=59816&extra=page%3D1&page=1
"""
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QWidget()
first_window.resize(400, 300)
first_window.setWindowTitle("我的第一个程序")
first_window.show()
sys.exit(app.exec_())

"""每一个PyQt5程序都需要有一个application对象，application类包含在QtGui模块中。
sys.argv参数是一个命令行参数列表。
Python脚本可以从shell中执行，参数可以让我们选择启动脚本的方式。
"""

