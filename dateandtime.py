import time
import datetime as dt
import json
import logging
import random

##logging.basicConfig(level=logging.DEBUG)

try:
    timefile = open("remindtimes.json", "r+")
    jfile = json.load(timefile)
except:
    raise FileNotFoundError

def validate_time(input: str, context: str):
# input is the time to be validated
# context is a string representing the menu validate_time() is accessed from (view time, delete time, etc)
    input = input.strip()

    def inc_format():
        print("incorrect format")
        if context == "input":
            term_time()
        elif context == "delete":
            del_time_term()

    try:
        logging.debug(f"Received time: \'{input}\'")

        # make sure there's exactly 4 digits
        assert(input.isdigit())
        assert(len(input) == 4)

        # get hours/minutes
        h_str = input[0:2]
        logging.debug("split h")
        m_str = input[2:4]
        logging.debug(f"h: {h_str}, m: {m_str}")

        # make sure hours/mins are still ints
        h_int, m_int = int(h_str), int(m_str)
        assert(m_int > 0, m_int < 60)
        assert(h_int > -1, h_int < 24)
    except:
        inc_format()

def randomize_and_write_json_time(req_t: str):
    req_t = req_t[0:2] + ":" + req_t[2:4]
    ran_t = get_random_time(req_t)
    logging.debug("random time generated")
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
    logging.debug("json generated")

    # write to json
    with open("remindtimes.json", "r+") as jf:
        data = json.load(jf)
        jf.seek(0) # start at beginning
        jf.truncate() # erase file, since data contains all times
        data["times"].append(entry)
        json.dump(data, jf, indent=4)
        logging.debug("json dumped")       

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
    logging.debug(f"initial time generated: {h_int}:{m_ran}:{s_ran}")

    # handle minute under/over flow
    if m_ran < 0:
        h_int -= 1
        m_ran = m_ran + 60
    elif m_ran > 59:
        h_int += 1
        m_ran = m_ran - 60
    
    logging.debug(f"minute generated as {m_ran}")

    # handle hour under/over flow
    # will change if days are implemented
    if h_int == -1:
        h_int = 23
    elif h_int == 24:
        h_int = 0

    logging.debug(f"hour generated as {h_int}")
    logging.debug(f"final time generated as {h_int}:{m_ran}:{s_ran}")
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
            logging.debug(f"appending {t["requested_time"]}")
            times.append((t["requested_time"], t)) # (string time, json)
        
        if len(t) == 0:
            logging.debug("There aren't any alarms scheduled")
        else:
            times.sort()
            next_time = -1
            next_time_json = -1
            i = -1
            for t in times:
                logging.debug(f"Comparing {t[0]} and {ct}")
                if t[0] >= ct:
                    next_time = t[0]
                    next_time_json = t[1]
                    logging.debug(f"{next_time} is the next time")
                    break
            if next_time == -1:
                next_time = times[0][0]
                next_time_json = times[0][1]
                i = 0
                logging.debug(f"There aren't any other alarms scheduled for today. The next time is {next_time} tomorrow.")
            else:
                logging.debug(f"The next alarm is for {next_time}")
                i = 1

        return (i, next_time, next_time_json)


def time_as_seconds_integer(t:str):
    if len(t) != 8:
        print(t)
        raise ValueError

    h = int(t[0:2])
    m = int(t[3:5])
    s = int(t[6:8])
    
    logging.debug(f"h = {str(h)}, m = {str(m)}, s = {str(s)}")

    return((3600 * h) + (60 * m) + s)

def time_with_colon_from_four_ints(t: str):
    h = t[0:2]
    m = t[2:4]
    print(f"{h}:{m}")
    return(f"{h}:{m}")

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
    del_time_from_file(time_with_colon_from_four_ints(ans))
