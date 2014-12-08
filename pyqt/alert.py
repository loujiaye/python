#!/usr/bin/python3.4

import sys
import time
import PyQt4.QtGui as gui
import PyQt4.QtCore as core

app = gui.QApplication(sys.argv)

try:
    due = core.QTime.currentTime()
    message = "alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours , mins = sys.argv[1].split(":")
    due = core.QTime(int(hours) , int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock

while core.QTime.currentTime() < due:
    time.sleep(20)

label = gui.QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(core.Qt.SplashScreen)
label.show()
core.QTimer.singleShot(60000 , app.quit)
app.exec_()
