#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyQt sandbox


import sys
from QtImport import QApplication, QWidget


qt_app = QApplication(sys.argv)

main_widget = QWidget()
main_widget.resize(640, 480)

main_widget.setWindowTitle("Main window")
main_widget.show()

sys.exit(qt_app.exec_())
