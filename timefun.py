from datetime import datetime
import pytz


#fetch data
def fetch_data():
    #Get Timezones
    timezone_list = ["Asia/Kolkata", "Europe/Dublin"]

    #Create dictonary with all the data
    info_dict = {}
    for i in timezone_list:
        timezone = pytz.timezone(i) #Get timezone of the specific area
        info_dict.update({i : [datetime.now(timezone).strftime("%d:%m:%Y"), #Get date
                            datetime.now(timezone).strftime("%H:%M:%S")]}) #Get time

    #for printing
    #for key in info_dict:
    #    print(f"{key} : {info_dict[key][0], info_dict[key][1]}")

    return info_dict




