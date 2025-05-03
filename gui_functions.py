#Importing libraries
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Importing Other files
from time_functions import TimeZone

def create_timeZone_widget(timezoneName, parentWidget, x_pos, y_pos):

    t1 = TimeZone(timezoneName)

    timeZoneLabel1 = QLabel(parentWidget)
    timeZoneTime1 = QLabel(parentWidget)
    
    #TimeZone Name
    timeZoneLabel1.setText(t1.timezone)
    timeZoneTime1.setText(t1.fetch_current_time+ "   " + t1.fetch_current_date)

    timeZoneLabel1.move(x_pos,y_pos)
    timeZoneTime1.move(x_pos-10,y_pos+ 20)
    
    timeZoneLabel1.show()
    timeZoneTime1.show()

def window(timezoneNames):
    app = QApplication(sys.argv)
    w = QLabel()
    w.setWindowTitle("World Clock")
    w.setGeometry(100,100,600,300)

    #TODO:Create auto generative timezonewidget

    for i in range(len(timezoneNames)):
        create_timeZone_widget(timezoneName=timezoneNames[i],
                                parentWidget = w,
                                  x_pos=(i*200) + 50,
                                  y_pos=20)

    w.show()
    sys.exit(app.exec())
