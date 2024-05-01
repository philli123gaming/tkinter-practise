import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x800")
window.title("combo and spinponit")

items = [1, 2, 3, 4, 5]
item = tk.StringVar(value=items[0])
combobox = ttk.Combobox(master=window, textvariable=item)
combobox["values"] = items
# combobox.config(values=items)
# combobox.configure(values=items)
combobox.pack()

item_text = tk.StringVar(value=f"Selected item is {item.get()}")
label = tk.Label(window, text="Selected food: None")
label.pack()

combobox.bind("<<ComboboxSelected>>", lambda event: label.configure(text=f"Selected food is: {item.get()}"))

spinbox1 = ttk.Spinbox(master=window, from_=0, to=10,
                       increment=2)  # can do lambda for when a button is pressed using command
spinbox1.bind("<<Increment>>", lambda event: print("up arrow pressed"))
spinbox1.bind("<<Decrement>>", lambda event: print("down arrow pressed"))
spinbox1.pack()

spin_int = tk.IntVar(value=3)
spinbox2 = ttk.Spinbox(master=window, from_=0, to=10, increment=2, textvariable=spin_int,
                       command=lambda: print(spin_int.get()))
spinbox2.pack()

# challenge
values = ["a", "b", "c", "d", "e"]
current_item = tk.StringVar(value=values[0])
spinbox3 = ttk.Spinbox(window, values=values, textvariable=current_item)
spinbox3.bind("<<Decrement>>", lambda event: print(current_item.get()))
spinbox3.pack()

window.mainloop()
