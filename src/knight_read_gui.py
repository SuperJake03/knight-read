from tkinter import *
from tkinter import ttk


class KnightReadGUI:
    def __init__(self):
        root = Tk()
        root.title("Knight Read")

        mainframe = ttk.Frame(root)

        welcomeframe = ttk.Frame(
            mainframe,
            borderwidth=2,
            relief="raised",
        )

        welcomelabel = ttk.Label(
            welcomeframe,
            text="Welcome to Knight Read!",
            foreground="white",
            background="blue",
        ).grid()

        welcomeframe.grid()

        # uploadbutton = ttk.Button(mainframe, text="Upload File")
        # uploadbutton.grid()

        mainframe.pack()

        root.mainloop()
