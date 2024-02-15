from win11toast import toast
import datetime as dt
from datetime import *
import random

def notif():
    toast("Focus check-in")

def random_time(t):
    sec = 0

    min = t.minute
    hour = t.hour

    ##reminders within 5 minutes of midnight are not random, i don't wanna deal with day change crap
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

def string_time(t):
    h = t.hour
    m = t.minute
    mer = "am"
    if (h > 12):
        mer = "pm"
    if (m < 10):
        m = "0" + str(m)

    s = (str(h) + ":" + str(m) + mer)
    return(s)

# def randomize_times(times):
#     for count, t in enumerate(times):
#         t = random_time(t)
#         times.pop(count)
#         times.insert(count, t)


# def to_military_time(h, m, mer):
#     if (mer == "am" and h == 12):
#         h = 0
#     if (mer == "pm"):
#         h = int(h)
#         h += 12
#     m = int(m)
#     return dt.time(h, m, 0)
