#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from QtImport import QApplication, QWidget
 
a = QApplication(sys.argv)       
 
w = QWidget()
w.resize(640, 480)

print ("Added from master")
print ("Added from 1.0")
print ("Added from master2")
print ("1.0_0")
print ("master_0")

w.setWindowTitle("Main window") 
w.show() 
 
sys.exit(a.exec_())
