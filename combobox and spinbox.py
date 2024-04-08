
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

window = tk.Tk()
window.geometry("600x800")
window.title("Empty template used")


combobox = ttk.Combobox(master=window)
combobox.pack()

textstringvar = ttk.StringVar(value= "Selected Item: None")
text = tk.Text(master=window, text="Selected Item: None")
text.pack()

spinbox1 = ttk.Spinbox(master=window)
spinbox1.pack()

spinbox2 = ttk.Spinbox(master=window)
spinbox2.pack()

window.mainloop()
    