#!/usr/bin/python3
##author: wy
##2014-04-17
################

import os
import platform
import sys

from PyQt.QtGui import *
from PyQt.QtCore import *

import helpform
import newimagelg
import qrc_resouces

__VERSION__ = "1.0.0"

class MainWindow(QMainWindow):
    def __init__(self , parent=None):
        super(MainWindow ,self).__init__(parent)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200 , 200)
        self.imageLable.setAlignment(Qt.AlignCenter)
        self.imageLable.setContextMenuPolicy(Qt.ActionContextMenu)
        self.setContralWidget(self.imagetLabel)

        logDockWidget = QDockWidget("Log" , self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowArea(Qt.LeftDockWidgetArea |
                Qt.RightDockWidgetArea)
        self.listWidget(QListWidget)
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea , logDockWidget)
        

