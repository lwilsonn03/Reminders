'''
Main
'''

from desktop_notifier import DesktopNotifier
import asyncio
import sys
import dateandtime as cdt  # "custom date time"
import util
import notif

async def async_input(prompt=""):
    # Run the blocking input() in a separate thread
    return await asyncio.to_thread(input, prompt)

async def run_menu():
    while True:
        option_a = "1.send toast"
        option_b = "2.add time"
        option_c = "3.view times"
        option_d = "4.delete time"
        print(f"options: {option_a}  {option_b}  {option_c} {option_d} 0.quit")
        choice = await async_input("")  # Use async_input for non-blocking input
        match choice:
            case "1":
                msg = await async_input("msg: ")  # Asynchronous input for the message
                await notif.notif(msg)  # Directly await the notif coroutine
            case "2":
                cdt.term_time()
            case "3":
                cdt.view_times()
            case "4":
                cdt.del_time_term()
            case "0":
                sys.exit()
            case _:
                print("invalid")

async def on_start():
    util.new_line(3)
    print("Reminder app")
    print("")
    asyncio.create_task(notif.time_checker())
    await run_menu()

# Start the main program
asyncio.run(on_start())
