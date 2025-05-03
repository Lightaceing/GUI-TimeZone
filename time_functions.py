#Importing libraries
from datetime import datetime
import pytz

class TimeZone:
    def __init__(self, timezoneName):
        self.timezone = pytz.timezone(timezoneName)
        #self.timeZoneData = [timezoneName] + fetch_timezone_data(timezoneName)

    def fetch_current_time(self):
        print(datetime.now(self.timezone).strftime("%H:%M:%S"))

    def fetch_current_date(self):
        print(datetime.now(self.timezone).strftime("%d:%m:%Y"))

    
