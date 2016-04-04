#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
 
a = QApplication(sys.argv)       
 
w = QWidget()
w.resize(320, 240)
 
w.setWindowTitle("Main window") 
w.show() 
 
sys.exit(a.exec_())
