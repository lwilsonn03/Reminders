import tkinter as tk
from tkinter import font as tkFont
from tkinter import *
from tkinter import ttk
import reminders as rem
import datetime as dt
from datetime import *
import sys
import threading


def initialize():
    global window
    window = tk.Tk()
    window.title("Reminders")

    defaultFont = tkFont.nametofont("TkDefaultFont")
    defaultFont.configure(size=22, family="Arial")

    global body_font
    body_font = tkFont.Font(family="Helvetica", size=14, weight=NORMAL)

    global small_font
    small_font = tkFont.Font(family="Helvetica", size = 11, weight=NORMAL)

    run_main_screen()
    window.protocol("WM_DELETE_WINDOW", rem.close_program)
    window.mainloop()





def run_main_screen(*args):
   destroy_active_frames()
   main_screen_frame = tk.Frame(master=window, padx=20, pady=20) 

   start_button = tk.Button(text="Start", master=main_screen_frame, padx=10, pady=10)
   zen_mode_button = tk.Button(text="Zen Mode", master=main_screen_frame, padx=10, pady=10)
   edit_times_button = tk.Button(text="Edit Times", master=main_screen_frame, padx=10, pady=10)
   quit_button = tk.Button(text="Quit", master=main_screen_frame, padx=10, pady=10)

   main_screen_label = tk.Label(text="Reminders", master=main_screen_frame, padx=20, pady=20)
   main_screen_frame.grid()
   main_screen_frame.grid_columnconfigure(0, minsize=30)
   main_screen_frame.grid_columnconfigure(4, minsize=30)

   #grid components
   main_screen_label.grid(column=2, columnspan=3, row=0)

   start_button.grid(column=2, columnspan=3, row=1)
   zen_mode_button.grid(column=2, row=2)
   edit_times_button.grid(column=2, row = 3)
   quit_button.grid(column=2, row = 4)

   def do_start_button(event):
      rem_thread = threading.Thread(target = rem.unsuspend)
      screen_thread = threading.Thread(target=run_operating_screen)
      rem_thread.start()
      screen_thread.start()
   #bind buttons
   start_button.bind("<Button-1>", do_start_button)
#    zen_mode_button.bind("<Button-1>", )
   edit_times_button.bind("<Button-1>", run_edit_screen)
   quit_button.bind("<Button-1>", rem.close_program)

def run_edit_screen(event):
   destroy_active_frames()
   edit_frame = tk.Frame(master=window, padx=20, pady=20)
   big_edit_label = tk.Label(text="Edit Times:", master=edit_frame, padx=20, pady=20)
   instructions_edit_label = tk.Label(text="Enter a new line between each time\nHH:MM or HH:MM a/pm", master=edit_frame, font=body_font)
   edit_text_box = tk.Text(master=edit_frame, height=12, width=35, font=body_font)
   confirm_edit_button = tk.Button(text="Confirm", master=edit_frame, padx=5, pady=5)

   try:
      edit_box_times = open("remindtimes.txt", "r+")
      edit_box_times = edit_box_times.read()
   except:
      raise Exception("Could not access file")
   
   edit_text_box.insert(INSERT, edit_box_times)
   
   #gridding
   edit_frame.grid()
   edit_frame.columnconfigure(0, minsize=35)
   edit_frame.columnconfigure(4, minsize=35)

   def finish_edit_times(event):
      user_time_text = edit_text_box.get(1.0, "end-1c")
      user_time_text = user_time_text.splitlines()
      remind_file = open("remindtimes.txt", "r+")
      old_times = remind_file.read()
      remind_file.close()
      remind_file = open("remindtimes.txt", "w")
      remind_file.write("")
      remind_file.close()
      remind_file = open("remindtimes.txt", "a")
      for t in user_time_text:
         if t in old_times:
            remind_file.write(t + "\n") #if the time was already in the file, don't randomize again
         else:
            t = rem.string_to_time(t) #take as time object, randomize, and put back as string
            t = rem.random_time(t)
            t = rem.time_to_string(t)
            remind_file.write(t + "\n")
      run_main_screen()

   big_edit_label.grid(columnspan=3, row=0, column=1)
   instructions_edit_label.grid(columnspan=3, row =1, column=1)
   edit_text_box.grid(columnspan=3, row=2, column=1)
   confirm_edit_button.grid(row=3, column=2)
   confirm_edit_button.bind("<Button-1>", finish_edit_times)
   
def run_operating_screen(*args):

   destroy_active_frames()
   oper_frame = tk.Frame(master=window, padx=20, pady=20)
   oper_label = tk.Label(text="Running...", master=window, padx=20, pady=20)
   back_button = tk.Button(text ="Menu", master=window, padx=5, pady=5)
   suspend_button = tk.Button(text="Suspend", master=window, padx=5, pady=5)
   suspend_label = tk.Label(text="Program Suspended", master=window, padx=5, pady=5, font=small_font)
   resume_button = tk.Button(text="Resume", master=window, padx=5, pady=5)
   
   oper_frame.grid()
   oper_frame.columnconfigure(1, minsize=35)
   oper_label.grid(columnspan=3, rowspan=2, row=0, column=0)
   back_button.grid(row=2, column=0)
   suspend_button.grid(row=2, column=2)

   def do_suspend_button(event):
      rem.do_suspend()
      suspend_label.grid(columnspan=3, row=3, column=0)
      suspend_button.grid_remove()
      resume_button.grid(row=2, column=2)
      
   
   def do_resume_button(event):
      suspend_label.grid_remove
      resume_button.grid_remove()
      suspend_button.grid(row=2, column=2)

   back_button.bind("<Button-1>", run_main_screen)
   suspend_button.bind("<Button-1>", do_suspend_button)
   resume_button.bind("<Button-1>", do_resume_button)


def destroy_active_frames():
   for child in window.winfo_children():
      child.destroy()



