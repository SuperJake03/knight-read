from tkinter import *
from tkinter import ttk


class KnightReadGUI:
    def __init__(self):
        root = Tk()
        root.title("Knight Read")

        mainframe = ttk.Frame(root)

        label = ttk.Label(
            mainframe,
            text="Welcome to Knight Read!",
            foreground="white",
            background="black",
        )
        label.pack()

        uploadbutton = ttk.Button(mainframe, text="Upload File")
        uploadbutton.pack()

        mainframe.pack()

        root.mainloop()
