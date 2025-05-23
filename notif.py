import asyncio
from desktop_notifier import DesktopNotifier
from datetime import datetime as dt  
import dateandtime as cdt                    
import json
import logging


notifier = DesktopNotifier()
##logging.basicConfig(level=logging.DEBUG)

async def notif(msg="default message"):
    await notifier.send(title = "test notif", message = msg)
    await asyncio.sleep(1) # don't send more than one notif per second


async def time_checker():
    while True:
        logging.debug("time checked")
        next_time_tuple = cdt.get_next_time()
        next_time = next_time_tuple[1]
        indc = next_time_tuple[0]
        nt_json = next_time_tuple[2]
        ct = dt.now().time()
        ct_str = cdt.time_string_from_ints(ct.hour, ct.minute, ct.second)
        print(f"current time: {ct_str}, next time: {nt_json["actual_time"]}")
        ct_int = cdt.time_as_seconds_integer(ct_str)
        next_time_int = cdt.time_as_seconds_integer(nt_json["actual_time"])

        # when to check time more frequently than a minute: when the time is less than a minute away
        if ct_int > next_time_int - 60 and ct_int < next_time_int + 1:
            if ct_int == next_time_int:
                await notif()
                continue
            await asyncio.sleep(0.8)
        else:
            await asyncio.sleep(59)




    
        


