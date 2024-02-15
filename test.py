import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()

start_button = tk.Button(text="start")


def the_thing(event):
    vals1 = ["a", "b"]
    vals2 = ["c", "d"]

    var1 = StringVar()
    var2 = StringVar()

    box1 = ttk.Combobox(values=vals1, textvariable=var1)
    box2 = ttk.Combobox(values=vals2, textvariable=var2)

    def button_click(event):
        x = var1.get()
        y = var2.get()
        print(x, y)

    button = tk.Button(text="enter")
    button.bind("<Button-1>", button_click)



    box1.grid(row=0)
    box2.grid(row=1)
    button.grid(row=2)

start_button.bind("<Button-1>", the_thing)
start_button.grid()

window.mainloop()   