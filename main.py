from gui_functions import window
#from time_functions import fetch_timezone_data

"""
__name__ is interpret as __main__ when the file in run directly
__name__ is interpret as the name of the file if its being called in a file which has been imported.
"""
if __name__ == "__main__":

    window(timezoneNames = ["Asia/Kolkata","Europe/Vienna" ])