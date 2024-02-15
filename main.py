import tkinter as tk
from tkinter import font as tkFont
from tkinter import *
from tkinter import ttk
import reminders as rem
import datetime as dt
from datetime import *

##############
remind_times = [dt.time(12, 1, 1)]
##############

window = tk.Tk()
window.title("Reminders")
frame = tk.Frame(master=window)
frame.grid(padx=20, pady=20)

defaultFont = tkFont.nametofont("TkDefaultFont")
defaultFont.configure(size=18)

start_button = tk.Button(text="Start", master=frame)
end_button = tk.Button(text="Suspend", master=frame)
new_rem_button = tk.Button(text="New Reminder", master=frame)


start_button.grid(row = 0, column=0, padx=20, pady=20)
end_button.grid(row=0, column=2, padx=20, pady=20)
new_rem_button.grid(row=0, column=1, padx=20, pady=20)



def startProgram(event):
    rem.focusCheckIn()

def close_program(event):
    window.destroy()

def enter_new_reminder(event):
    ##create frames
    new_rem_frame = tk.Frame(master=window)

    #dismiss home screen
    frame.grid_forget()


    label_enter_text = tk.Label(text="Enter time:")
    label_enter_text.grid(columnspan=3, row=0)


    ##configure hour info
    nh = StringVar()
    hour_options = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ]
    box_hour = ttk.Combobox(master=new_rem_frame, values=hour_options, textvariable=nh, width=3, font=defaultFont, state="readonly")
    label_hour = tk.Label(text="Hour:", master=new_rem_frame)
    label_hour.grid(row=1, column=0, padx=5, pady=5)


    ##configure minute info
    nm = StringVar()
    minute_options = [
        "00", "05", 10, 15, 20, 25, 30, 35, 40, 45, 50, 55
    ]
    box_minute = ttk.Combobox(master=new_rem_frame, values=minute_options, textvariable=nm, width=3, font=defaultFont, state="readonly")
    label_minute = tk.Label(text="Min:", master=new_rem_frame)
    label_minute.grid(row=1, column=1, padx=5, pady=5)


    ##configure am/pm
    nmer = StringVar()
    meridians = [
        "am", "pm"
    ]
    box_meridian = ttk.Combobox(master=new_rem_frame, values=meridians, textvariable=nmer, width=3, font=defaultFont, state="readonly")
  

    ##configure accept button
    def add_time(event):
        x = int(nh.get())
        y = int(nm.get())
        z = nmer.get()
        if (z == "am" and x == 12):
            x = 0
        if (z == "pm" and x < 12):
            x += 12
        tm = dt.time(x, y, 0)
        tm = rem.random_time(tm)
        remind_times.append(tm)
        new_rem_frame.grid_forget()
        frame.grid(padx=20, pady=20)

    new_time_button = tk.Button(text="Enter", master=new_rem_frame, padx=5, pady=5)
    new_time_button.bind("<Button-1>", add_time)


    ##grid em up
    box_hour.grid(row=2, column=0, padx=5, pady=5)
    box_meridian.grid(row=2, column=2, padx=5, pady=5)
    box_minute.grid(row=2, column=1, padx=5, pady=5)
    new_time_button.grid(row=3, columnspan=3)
    new_rem_frame.grid(padx=5, pady=5)


start_button.bind("<Button-1>", startProgram)
new_rem_button.bind("<Button-1>", enter_new_reminder)
end_button.bind("<Button-1>", close_program)

window.mainloop()





