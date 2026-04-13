from tkinter import *
from tkinter import ttk
from unittest.main import main


class KnightReadGUI:
    def __init__(self):
        # Root Window
        root = Tk()
        root.title("Knight Read")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Main frame to put all other frames into.
        mainframe = ttk.Frame(root, padding=3)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(2, weight=1)

        # All container frames
        welcomeframe = ttk.Frame(
            mainframe,
            borderwidth=5,
            relief="ridge",
            # width=1000,
            # height=100,
        )
        uploadframe = ttk.Frame(
            mainframe,
            borderwidth=5,
            relief="ridge",
            width=300,
            height=100,
        )
        libraryframe = ttk.Frame(
            mainframe,
            borderwidth=5,
            relief="ridge",
            width=300,
            height=300,
        )

        # Layout of container frames
        welcomeframe.grid(column=0, row=0, sticky=(W, E))
        uploadframe.grid(column=0, row=1, sticky=(W, E))
        libraryframe.grid(column=0, row=2, sticky=(N, W, E, S))

        # Welcome frame widgets
        welcomelabel = ttk.Label(
            welcomeframe,
            text="Welcome to Knight Read!",
        )
        welcomelabel.grid(column=0, row=0, pady=20)
        welcomeframe.columnconfigure(0, weight=1)

        root.mainloop()
