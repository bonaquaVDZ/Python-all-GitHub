
import tkinter
from tkinter.constants import *
from tkinter import *
tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH,   expand=1)

label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=2)

button = tkinter.Button(frame,  text="Exit",    command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()


print("----------------------------------------------------------------------")


pattern = Tk()

window = tkinter.Label(pattern, text="Hello, world!")
window.pack()

pattern.mainloop()

help("tkinter.Label.__init__")
