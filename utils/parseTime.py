from datetime import datetime

def parse_time(time): 
    return datetime.strptime(time, "%H:%M:%S").time()

