#!/usr/bin/python3
##author: wy
##2014-28-39
################


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def setPenProperties(self):
    dialog = PenPropertiesDlg(self)
    dialog.widthSpinBox.setValue(self.width)
    dialog.beveledCheckBox.setChecked(self.beveled)
    dialog.styleComboBox.setCurrentIndex(1)
    
    print("begin")
    print(dialog.exec_())
    print("end")

    if dialog.exec_():
        self.width = dialog.widthSpinBox.value()
        self.beveled = dialog.beveledCheckBox.isChecked()
        self.style = str(dialog.styleComboBox.currentText())
        
        print(self.width , self.beveled , self.style)

class PenPropertiesDlg(QDialog):
    def __init__(self , parent=None):
        super(PenPropertiesDlg , self).__init__(parent)

        widthLabel = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.widthSpinBox.setRange(0 , 24)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        styleLabel = QLabel("&Style")
        self.styleComboBox = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid" , "Dashed" , "Dotted" ,
            "DashDotted" ,"DashDotDotted"])
        okButton = QPushButton("&确定")
        cancelButton = QPushButton("取消")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthLabel , 0 , 0)
        layout.addWidget(self.widthSpinBox , 0 , 1)
        layout.addWidget(self.beveledCheckBox , 0 , 2)
        layout.addWidget(styleLabel , 1 , 0 )
        layout.addWidget(self.styleComboBox ,  1 , 1  , 1 , 2)
        layout.addLayout(buttonLayout , 2 , 0 ,  1 , 3)
        self.setLayout(layout)

        self.connect(okButton , SIGNAL("clicked()") , self , SLOT("accept()"))
        self.connect(cancelButton ,SIGNAL("clicked()") , self ,
                SLOT("accept()"))
        self.setWindowTitle("pen property")

class Blank(QDialog):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    self = Blank()
    self.width = 4
    self.beveled = True
    
    setPenProperties(self)
