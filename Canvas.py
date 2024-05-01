import tkinter as tk
from tkinter import ttk


# https://tkdocs.com/tutorial/canvas.html
window = tk.Tk()
window.geometry("600x800")
window.title("Canvas")

# essentially microsoft paint in python
Canvas = tk.Canvas(window, bg="grey")
# Canvas.create_rectangle((0,0,100,200),#needs tuple of left top right and  bottom values width refers to border width
# fill="green",
# width=0,
# dash=(2,1),#first is how long each dash should be second is gap length
# outline = "green") #dash colour
# Canvas.create_line((0,0,300,250)) #needs a start x and y and end x and y in tuple
# Canvas.create_polygon((0,0,100,200,300,50)) #needs many points x1, y1, x2, y2, x3, y3 coordinates of each point negatives are possible too
#Canvas.create_oval((200, 0, 300, 100),fill="red")
#Canvas.create_arc((200, 0, 300, 100), fill="Green", start=100, extent= 30,style = tk.ARC, outline = "yellow", width = 10)
#Canvas.create_text((100,200), text="here is my text")
#Canvas.create_window((50,100), window=ttk.Label(window,text="text in canvas"))
def draw_on_canvas(event):
    global brush_size
    x = event.x
    y = event.y
    Canvas.create_oval((x - brush_size /2, y-brush_size/2, x+brush_size/2, y + brush_size/2), fill="green")

def update_brush_size(new_size):
    global brush_size
    brush_size = int(new_size)


def brush_adjust_size(event):
    global brush_size
    adjust_window = tk.Tk()
    adjust_window.geometry("200x200")

    start_var = tk.IntVar(adjust_window,value=brush_size)


    spinbox = ttk.Spinbox(adjust_window, from_=1,
                          to=20,
                          textvariable=start_var,
                          command=lambda: [print(spinbox.get()),update_brush_size(spinbox.get())])
    spinbox.pack()

    adjust_window.mainloop()


brush_size = 4
Canvas.bind("<Motion>", draw_on_canvas)
Canvas.bind("<Button-2>", brush_adjust_size)
Canvas.pack()

window.mainloop()
