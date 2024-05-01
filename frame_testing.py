
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter import font
    
window = tk.Tk()
window.geometry("600x800")
window.title("Empty template used")

style1 = font.Font(size=20)
style2 = font.Font(size=25)

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

page1.grid(row=0,column=0,sticky="nsew")
page2.grid(row=0,column=0,sticky="nsew")
page3.grid(row=0,column=0,sticky="nsew")

lb1 = Label(page1, text="I am page 1", font=style1)
lb1.pack(pady=20)

lb2 = Label(page2, text="I am page 2", font=style1)
lb2.pack(pady=20)

lb3 = Label(page3, text="I am page 3", font=style1)
lb3.pack(pady=50)

btn1 = Button(page1, text="show page 2", command=lambda: page2.tkraise(), font=style2)
btn1.pack(side="left", padx=50)

btn2 = Button(page2, text="show page 1", command=lambda: page1.tkraise(), font=style2)  #|
btn2.pack(side="left")                                                                             #| these 2 buttons are on page 2
                                                                                        #|
btn3 = Button(page2, text="show page 3", command=lambda: page3.tkraise(), font=style2)  #|
btn3.pack(side="left")

btn4 = Button(page3, text="show page 2", command=lambda: page2.tkraise(), font=style2)  #|
btn4.pack(side="left")

btn5 = Button(page3, text="show page 1", command=lambda: page1.tkraise(), font=style2)  #|
btn5.pack(side="left")
page1.tkraise() #Raises this frame to the top


window.mainloop()

root = Tk( )
b=0
for r in range(6):
  for c in range(6):
     b=b+1
     Button(root, text=str(b),
        borderwidth=1 ).grid(row=r,column=c)
root.mainloop()