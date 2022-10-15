from datetime import datetime

def parseTime(time): 
    return datetime.strptime(time, "%H:%M:%S").time()

