#!/usr/bin/python3

import sys
import math
import PyQt4.QtGui as gui
import PyQt4.QtCore as core

class Form(gui.QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.browser = gui.QTextBrowser()
        self.lineedit = gui.QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout =  gui.QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect(self.lineedit , core.SIGNAL("returnPressed()") , self.updateUi)
        self.setWindowTitle("Calculate")
        
    def updateUi(self):
        try :
            text = str(self.lineedit.text())
            self.lineedit.clear()
            self.browser.append("%s = <b>%s</b>" %(text , eval(text)))
        except :
            self.browser.append("<font color=red>%s is invalid" % text)


app = gui.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
