import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk #ttkbootstrap is essentially an extended module with more design features and simplified functions


def button_func():
    inputfiled_input = inputfield1.get()
    print(inputfiled_input)

    #to update labels
    #Label.configure(text=inputfiled_input)
    Label["text"] = inputfiled_input #preferred method
    inputfield1["state"] = "disabled" #disables it
    print(inputfield1.configure()) #prints al changable attribbutes of the widget via index method

def revert_label():
    Label["text"] = "Some text"  # preferred method
    inputfield1["state"] = "enabled"  # enables it
window = ttk.Window()
window.title("Windows and Widgets")
window.geometry("600x800")
Labelstr = ttk.StringVar
Label = ttk.Label(master=window, text="this is a label")
Label.pack()
inputfield1 = ttk.Entry(width=400, master=window)
inputfield1.pack()
inputfield2 = ttk.Entry(master=window)
inputfield2.pack()
button1 = ttk.Button(master=window, text="A button", command=button_func)
button1.pack()
button2 = ttk.Button(master=window, text="Revert", command=revert_label)
button2.pack()
window.mainloop()