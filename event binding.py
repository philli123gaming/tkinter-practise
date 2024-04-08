import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def get_pos(event):
    print(f"x:{event.x} y:{event.y}")

window = tk.Tk()
window.title("Event binding")
window.geometry("600x800")

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window)
button.pack()

#events use the bind with the first argument in the format "<modifier-type-detail>"
button.bind("<Alt-KeyPress-a>", lambda event: print(event))
#window.bind("<Motion>", lambda event: get_pos(event)) #gives constant mouse position #I can bind this only to text so It will only track the motion to whatever widget its binded too
#window.bind("<KeyPress>", lambda event: print(f"a button was pressed at {event.char}")) # event.char returns the key press if widget was selected

text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel")) #prints "mousewheel" when the user holds down shift and uses the mousewheel with text selected

#when binding an event if I use a function it automatically passes an argument, and so I need to maek a parameter to catch this argument before it causes an error
#will only work if the selected widget is selected
window.mainloop()

#https://www.pythontutorial.net/tkinter/tkinter-event-binding/ an event list