from win11toast import toast
import datetime as dt
from datetime import *
import time
import random
import re
import threading
import sys

remind_times = ""
global suspend
suspend = False

try:
    remind_file = open("remindtimes.txt", "r+")
    remind_times = remind_file.read()
except:
    raise Exception("Failed to access file")

def do_suspend():
    global suspend
    suspend = True

def unsuspend():
    global suspend
    suspend = False
    begin_notif_time()

def check_suspend():
    global suspend
    return suspend

def close_file():
    remind_file.close()

def notif():
    toast("Focus check-in")

def random_time(t):
    sec = 0

    min = t.minute
    hour = t.hour

    ##reminders within 5 minutes of midnight are not random, I don't want to worry about day change
    if (hour == 0 and min <= 5):
        return dt.time(hour, min, sec)
    if (hour == 23 and min >= 55):
        return dt.time(hour, min, sec)

    ##randomize +/- 5 minutes
    min = min + random.randint(-5, 5)
    if (min >= 60):
        min = min - 60
        hour += 1
    if (min < 0):
        min = min + 60
        hour -= 1
    sec = random.randint(0, 59)
    return dt.time(hour, min, sec)

def time_to_string(t):
    h = t.hour
    m = t.minute
    if (m < 10):
        m = "0" + str(m)
    s = (str(h) + ":" + str(m))
    return(s)

def string_to_time(s):
    alpha = re.findall("[a-zA-Z]", s) 
    s = re.split('[:]', s)   
    h = int(re.findall("[0-9]", s[0]))
    m = int(re.findall("[0-9]", s[1]))
    if (alpha != ""):
        ap = s[2].lower()
    if (ap == "am" and h == 0):
        h = 12
    if (ap == "pm" and h != 12):
        h += 12
    
    t = dt.time(h, m, 0)
    return t

def begin_notif_time():
    suspend = False
    while (not suspend):
        curr_time = datetime.now()
        rem_times = open("remindtimes.txt", "r+")
        rem_times = rem_times.read()
        rem_times = rem_times.splitlines(True)
        for t in rem_times:
            print("Testing time " + t)
            t = string_to_time(t)
            curr_time = dt.time(curr_time.hour, curr_time.minute, 0)
            print("current time: " + time_to_string(curr_time))
            if (t == curr_time):
                notif()
        time.sleep(1)
        suspend = check_suspend()



def close_program(*args):
   do_suspend()
   close_file()
   sys.exit(0)
