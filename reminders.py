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
    sec = random.randint(0, 59)
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
    return dt.time(hour, min, sec)



def time_to_string(t):
    h = t.hour
    m = t.minute
    if (m < 10):
        m = "0" + str(m)
    s = (str(h) + ":" + str(m))
    return(s)



def string_to_time(s):
    try:
        s = s.strip()
        mer = "" #meridiem (am/pm)
        alpha = re.findall("[a-zA-Z]", s) #extract mer from total
        for b in alpha:
            b = b.strip()
            mer += b
        s = re.split('[:]', s) #split hours from minutes
        for n, b in enumerate(s): #find digits, extract to string
            b = re.findall("[0-9]", s[n])
            s[n] = ""
            for m in b:
                s[n] += m
        h = int(s[0])
        if (mer != ""): #handle am/pm
            mer = mer.lower()
            if (mer == "am" and h == 0):
                h = 12
            if (mer == "pm" and h != 12):
                h += 12

        m =int(s[1])
        t = dt.time(h, m, 0)
        return t
    except:
        raise Exception("Error: unrecognized time format")



def begin_notif_time():
    suspend = False
    while (not suspend):
        curr_time = datetime.now()
        rem_times = open("remindtimes.txt", "r+")
        rem_times = rem_times.read()
        rem_times = rem_times.splitlines(True)
        for t in rem_times:
            t = string_to_time(t)
            curr_time = dt.time(curr_time.hour, curr_time.minute, 0)
            if (t == curr_time):
                notif()
        time.sleep(1)
        suspend = check_suspend()
    


def next_rem_time():
    curr_time = time_to_string(datetime.now())
    rem_times = remind_times.splitlines()
    for t in rem_times:
        if (t == curr_time):
            return "0"
        if (curr_time < t):
            return t
    return "-1" #no upcoming time



def next_rem_time_string():
    ans = next_rem_time()
    if (ans == "-1"):
        return "No reminders left today"
    if (ans == "0"):
        return "Now"
    else:
        return "Next reminder at " + ans
    


def close_program(*args):
   do_suspend()
   close_file()
   sys.exit(0)
