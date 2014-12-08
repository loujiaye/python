#!/usr/bin/python3
##author: wy
##2014-28-35
##

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dial , SIGNAL("valueChanged(int)") , spinbox.setValue)
        self.connect(spinbox , SIGNAL("valueChanged(int)"), dial.setValue)
        self.setWindowTitle("Signal and Slots")

class ZeroSpinBox(QSpinBox):
    zeros = 0
    
    def __init__(self , parent):
        super(ZeroSpinBox , self).__init__(parent)
        self.connect(self , SIGNAL("valueChanged(int)") , self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero") , self.zeros)

