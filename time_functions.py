#Importing libraries
from datetime import datetime
import pytz

def fetch_timezone_data(timezone_Name):
    timezone = pytz.timezone(timezone_Name)
    timezone_info = [datetime.now(timezone).strftime("%d:%m:%Y"), 
                     datetime.now(timezone).strftime("%H:%M:%S")]
    return timezone_info

class TimeZone:
    def __init__(self, timezoneName):
        self.timezone = timezoneName
        self.timeZoneData = [timezoneName] + fetch_timezone_data(timezoneName)



