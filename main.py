import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from timefun import fetch_data


def window(zone1, zone2):
    app = QApplication(sys.argv)
    w = QLabel()
    w.setWindowTitle("World Clock")
    w.setGeometry(100,100,600,300)

    #TimeZone1
    timeZoneLabel1 = QLabel(w)
    timeZoneLabel1.setText(zone1[0])
    timeZoneLabel1.move(50,20)

    timeZoneTime1 = QLabel(w)
    timeZoneTime1.setText(zone1[1]+ "   " + zone1[2])
    timeZoneTime1.move(40,50)
    #TimeZone2
    timeZoneLabel2 = QLabel(w)
    timeZoneLabel2.setText(zone2[0])
    timeZoneLabel2.move(300,20)

    
    timeZoneTime2 = QLabel(w)
    timeZoneTime2.setText(zone2[1]+ "   " + zone2[2])
    timeZoneTime2.move(300,50)


    w.show()
    timeZoneLabel1.show()
    timeZoneLabel2.show()
    timeZoneTime1.show()
    timeZoneTime2.show()
    sys.exit(app.exec())



"""
__name__ is interpret as __main__ when the file in run directly
__name__ is interpret as the name of the file if its being called in a file which has been imported.
"""
if __name__ == "__main__":
    info_dict = fetch_data()
    info_list_keys = list(info_dict.keys())
    zone1 = [info_list_keys[0], info_dict[info_list_keys[0]][0], info_dict[info_list_keys[0]][1]]
    zone2 = [info_list_keys[1], info_dict[info_list_keys[1]][0], info_dict[info_list_keys[1]][1]]

    #zone1 = [info_dict.keys[0], info_dict.values[info_dict.keys[0]][0], info_dict.values[info_dict.keys[0]][0]]
    #zone2 = [info_dict.keys[1], info_dict.values[info_dict.keys[1]][0], info_dict.values[info_dict.keys[1]][0]]
    window(zone1, zone2)