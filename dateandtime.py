import time
import datetime as dt
import json
import random

# Open the file
try:
    timefile = open("remindtimes.json", "r+")
    jfile = json.load(timefile)
except:
    raise FileNotFoundError

def validate_time(input: str, context: str):
# input is the time to be validated
# context is a string representing the menu validate_time() is accessed from (view time, delete time, etc)
    input = input.strip()

    # defines what the method does when it finds an incorrect time format
    def inc_format():
        print("incorrect format")
        match context:
            case "input":
                term_time()
            case "delete":
                del_time_term()
            case "format_time":
                raise ValueError("The entered time is invalid")

    try:
        # make sure there's exactly 4 digits
        assert(input.isdigit())
        assert(len(input) == 4)

        # get hours/minutes
        h_str = input[0:2]
        m_str = input[2:4]

        # make sure hours/mins are still ints
        h_int, m_int = int(h_str), int(m_str)
        assert(m_int > 0 and m_int < 60)
        assert(h_int > -1 and h_int < 24)
    except:
        inc_format()


def format_time(time, current_format: str, new_format: str):
# designed to handle all time format conversions.
# new_format and current_format should be one of the following values:
#   "hh:mm", HH:MM
#   "hhmm", HHMM
#   "hh:mm:ss" HH:MM:SS
#   "json", (requested time, actual time, hour, minute, second, message default, message(optional))
#   "seconds", time as seconds from midnight (useful for easy comparison of if a time is earlier/later than another)
           
# 1: convert the time to hours, minutes, seconds
    h, m, s = 0, 0, 0

    match(current_format):
        case "json":
            h = time["hour"]
            m = time["minute"]
            s = time["second"]
        case "hh:mm":
            h = int(time[0:2])
            m = int(time[3:5])
        case "hhmm":
            h = int(time[0:2])
            m = int(time[2:4])
        case "hh:mm:ss":
            h = int(time[0:2])
            m = int(time[3:5])
            s = int(time[6:8]) 
        case "seconds":
            time = int(time)
            h = int(time/3600)
            m = int((time-(h*3600))/60)
            s = int(time%60)
        case _:
            raise ValueError(f"current format string, {current_format}, was unrecognized")

# 2: validate h/m/s to ensure current_format matched time format
    try:
        assert(h >= 0 and h < 24)
        assert(m >= 0 and m < 60)
        assert(s >= 0 and s < 60)
    except:
        raise ValueError(f"current format was entered as {current_format}, but time {time} doesn't appear to match1")

# 3: convert to new time
    new_time = ""

    def add_zero(i: int):
        # adds leading zero if needed for string based times (ex. 9 -> 09)
        if i < 10 and i > -1:
            return f"0{i}"
        else:
            return i

    match(new_format):
        case "json":
            # if the new time should be json, more information is needed like what is the requested time vs actual alarm time?
            new_time = "placeholder"
        case "hh:mm":
            new_time = f"{add_zero(h)}:{add_zero(m)}"
        case "hhmm":
            new_time = f"{add_zero(h)}{add_zero(m)}"
        case "hh:mm:ss":
            new_time = f"{add_zero(h)}:{add_zero(m)}:{add_zero(s)}"
        case "seconds":
            new_time = ((h*3600) + (m*60) + s)
        case _:
            raise ValueError(f"new format string, {new_format}, was unrecognized")
    
    return new_time


def randomize_and_write_json_time(req_t: str):
    req_t = req_t[0:2] + ":" + req_t[2:4]
    ran_t = get_random_time(req_t)
    h, m, s = ran_t[0], ran_t[1], ran_t[2]

    # prepare json entry
    entry = {
        "requested_time" : req_t,
        "actual_time" : time_string_from_ints(h, m, s),
        "hour" : h,
        "minute" : m,
        "second" : s,
        "message_default" : True
    }

    # write to json
    with open("remindtimes.json", "r+") as jf:
        data = json.load(jf)
        jf.seek(0) # start at beginning
        jf.truncate() # erase file, since data contains all times
        data["times"].append(entry)
        json.dump(data, jf, indent=4)

# prints times in a nice format to the terminal
def view_times():
    print("\nYou have reminders set for: ")
    with open("remindtimes.json", "r") as jf:
        data = json.load(jf)
        for t in data["times"]:
            print(t["requested_time"])    

# returns tuple of (hour, minute, second) randomized
def get_random_time(t: str):
    # get minute and hour ints
    h_int, m_int = int(t[0:2]), int(t[3::])

    # get randomized minutes and seconds
    # will be checked/modified shortly
    rand_scale = 5 # randomize by how many minutes?
    m_ran, s_ran = (random.randint(-rand_scale,rand_scale) + m_int), random.randint(0,59)

    # handle minute under/over flow
    if m_ran < 0:
        h_int -= 1
        m_ran = m_ran + 60
    elif m_ran > 59:
        h_int += 1
        m_ran = m_ran - 60
    

    # handle hour under/over flow
    # will change if days are implemented
    if h_int == -1:
        h_int = 23
    elif h_int == 24:
        h_int = 0
    return (h_int, m_ran, s_ran)

def time_string_from_ints(h:int, m:int, s:int=0):
    if h < 10:
        h = f"0{h}"
    if m < 10:
        m = f"0{m}"
    if s < 10:
        s = f"0{s}"
    return f"{h}:{m}:{s}"


def term_time():
    print("enter 4 integers as a time. For example, 0906 is 9:06am")
    ans = input("input time: ")
    validate_time(ans, "input")
    randomize_and_write_json_time(ans)


def get_next_time(ct=str(dt.datetime.now().hour) + ":" + str(dt.datetime.now().minute)):
    # indicator is -1 if no times, 0 if next time is tomorrow, 1 if there is a time today
    # returns (indicator, string, json) 

    with open("remindtimes.json", "r+") as jf:
        data = json.load(jf)
        times = []
        for t in data["times"]:
            times.append((t["requested_time"], t)) # (string time, json)
        
        if len(t) != 0:
            times.sort()
            next_time = -1
            next_time_json = -1
            i = -1
            for t in times:
                if t[0] >= ct:
                    next_time = t[0]
                    next_time_json = t[1]
                    
                    break
            if next_time == -1:
                next_time = times[0][0]
                next_time_json = times[0][1]
                i = 0
            else:
                i = 1

        return (i, next_time, next_time_json)


def del_time_from_file(t:str):
# t should be received as HH:MM
    with open('remindtimes.json', 'r') as jf:
        data = json.load(jf)
        data["times"] = [entry for entry in data["times"] if entry["requested_time"] != t]
    with open('remindtimes.json', 'w') as jf:
        json.dump(data, jf, indent=4)


def del_time_term():
    view_times()
    ans = input("Delete a time by entering its value as 4 integers: ")
    validate_time(ans, "delete")
    ans = format_time(ans, "hhmm", "hh:mm")
    del_time_from_file(str(ans))
