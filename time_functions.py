#Importing libraries
from datetime import datetime
import pytz

class TimeZone:
    def __init__(self, timezoneName):
        self.timezone = pytz.timezone(timezoneName)

    def fetch_current_time(self):
        return datetime.now(self.timezone).strftime("%H:%M:%S")

    def fetch_current_date(self):
        return datetime.now(self.timezone).strftime("%d:%m:%Y")

    