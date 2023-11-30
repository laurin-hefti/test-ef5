from datetime import datetime

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
    time = time[0:8]
    day = str(int(day)-1)
    time += day
    return time