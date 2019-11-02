# Program to display Clock Widget using tkinter

import tkinter as tk

from time import strftime

top = tk.Tk()
top.title('Clock')
top.resizable(0,0)

def time(): 
    string = strftime('%H:%M:%S %p') 
    clockTime.config(text = string) 
    clockTime.after(1000, time)

clockTime = tk.Label(top, font = ('Arial', 32, 'bold'), background = 'navyblue', foreground = 'white')

clockTime.pack(anchor = 'center')
time()

top.mainloop()
