
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

window = tk.Tk()
window.geometry("600x800")
window.title("Empty template used")

def createcheckbox():
    check_var = ttk.BooleanVar(value=False)  # starting value for the checkbox
    checkbox1 = ttk.Checkbutton(window, text="checkbox 1", variable=check_var)  # buttons have a variable attribute that contains the state of the checkbox which removes neutral
    checkbox1.pack()

button = ttk.Button(window, command=createcheckbox)
button.pack()
window.mainloop()
    