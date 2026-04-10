from tkinter import *
from tkinter import ttk


class KnightReadGUI:
    def __init__(self):
        root = Tk()
        root.title("Knight Read")

        mainframe = ttk.Frame(root)
        lbl = ttk.Label(mainframe, text="Welcome to Knight Read!")
        lbl.pack()

        mainframe.pack()

        root.mainloop()
