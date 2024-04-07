import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk #ttkbootstrap is essentially an extended module with more design features and simplified functions

def convertget(): # some widgets don't have get methods
    try:
        mile_input = int(entry1.get())
        km_output = mile_input*1.61
        print(f"{mile_input} Miles =  {km_output}")
        output_string_var.set(f"Output: {km_output}Km") # set method for container overwrites the current value so I can dynamically change text
    except ValueError:
        print("that wasn't a number")

def convertvar():
    try:
        print(int(entryintvar.get())*3)
    except ValueError:
        print("that wasn't a number")

#window
window = ttk.Window(themename="darkly") # or just tk.TK()
window.title("test window")
window.geometry("500x700")

# title
title_label = ttk.Label(master= window, text="miles to kilometers", font="Calibri 24 bold") #label means text apparently the master is the parent
title_label.pack()

#input field and button created which link to the convertget function
#input field
input_frame1 = ttk.Frame(master=window)
entry1 = ttk.Entry(master=input_frame1)
button1 = ttk.Button(master=input_frame1, text= "convert using get.()",command= convertget)
entry1.pack(side="left")
button1.pack(side="left", padx=10)
input_frame1.pack(pady = 20)

#input field and button created which link to the convertvar function by using premade variables
#input field
input_frame2 = ttk.Frame(master=window)
entryintvar = tk.IntVar()
entry2 = ttk.Entry(master=input_frame2, textvariable=entryintvar)
button2 = ttk.Button(master=input_frame2, text= "convert using int var",command= convertvar)
entry2.pack(side="left")
button2.pack(side="left", padx=10)
input_frame2.pack(pady = 20)

#output
output_string_var = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text = "output",
    font="Calibri 24",
    textvariable=output_string_var)
output_label.pack()
# run
window.mainloop()