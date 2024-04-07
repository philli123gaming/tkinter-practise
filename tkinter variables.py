import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk #ttkbootstrap is essentially an extended module with more design features and simplified functions

window = ttk.Window()
window.title("Tkinter variables")
window.geometry("600x800")


#tkinter variable
string_var = ttk.StringVar(value="test") #sets place holder #string var also has a set method


inputfield1 = ttk.Entry(width=400, master=window, textvariable=string_var)
inputfield2 = ttk.Entry(width=400, master=window, textvariable=string_var)
Label = ttk.Label(master=window, text="label", textvariable=string_var)

Label.pack()
inputfield1.pack()
inputfield2.pack()

window.mainloop()