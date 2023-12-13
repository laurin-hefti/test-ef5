from datetime import datetime

# functions for time handeling

def get_time():
    time = datetime.now()
    return time

def call_interval(t,t2):
    time = str(get_time().time())
    time = time[0:2]
    if int(time) >= t and int(time) < t2:
        return True
    else:
        return False
    
def get_date():
    time = str(get_time().date())
    day = time[8:10]
    month = time[5:8]
    time = time[0:5]
    day = str(int(day)-1)
    if len(month) == 1:
        month = "0"+month
    if len(day) == 1:
        day = "0"+day
    time += month
    time += day
    return time