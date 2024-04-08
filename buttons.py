import tkinter as tk
#from tkinter import ttk
import ttkbootstrap
import ttkbootstrap as ttk #ttkbootstrap is essentially an extended module with more design features and simplified functions


window = ttk.Window()
window.title("Buttons")
window.geometry("600x800")
buttontext = ttk.StringVar(value="button")
button = ttk.Button(window, text="button", textvariable= buttontext) # can pass only window and not master = window
button.pack()

check_var = ttk.BooleanVar(value=False ) #starting value for the checkbox
checkbox1 = ttk.Checkbutton(window, text="checkbox 1", command= lambda: print(check_var.get()), variable=check_var) #buttons have a variable attribute that contains the state of the checkbox which removes neutral
checkbox1.pack()
checkbox2 = ttk.Checkbutton(window, text="checkbox 2", variable=check_var)
checkbox2.pack()

radiobutton1 = ttk.Radiobutton(window, text="radio button 1", value= 1) # the buttons default value is 0 so if there are multiple radio buttons in with no value they will both go on
radiobutton1.pack()
radiobutton2 = ttk.Radiobutton(window, text="radio button 2", value= 3) # one radio button is usually always on
radiobutton2.pack()

checkbox3 = ttk.Checkbutton(window, text="checkbox 1", command= lambda: print(check_var.get()), variable=check_var) #buttons have a variable attribute that contains the state of the checkbox which removes neutral
checkbox3.pack()
checkbox4 = ttk.Checkbutton(window, text="checkbox 2", variable= check_var, command=lambda : check_var.set(True) if not check_var.set(True) else check_var.set(False) )
checkbox4.pack()
window.mainloop()