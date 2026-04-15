from pathlib import Path
from tkinter import *
from tkinter import filedialog, ttk


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
        welcomeframe = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        uploadframe = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
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
        welcomelabel = ttk.Label(welcomeframe, text="Welcome to Knight Read!")
        welcomelabel.grid(column=0, row=0, pady=20)
        welcomeframe.columnconfigure(0, weight=1)

        # Upload frame widgets
        uploadlabel = ttk.Label(uploadframe, text="Upload new EPUB here!")
        uploadbutton = ttk.Button(
            uploadframe, text="Select a file", command=self.upload_file
        )

        # Layout of upload frame widgets
        uploadlabel.grid(column=0, row=0, pady=5)
        uploadbutton.grid(column=0, row=1, pady=5)
        uploadframe.columnconfigure(0, weight=1)

        root.mainloop()

    def upload_file(self):
        file_types = [("EPUB files", "*.epub")]
        file_path = filedialog.askopenfilename(
            title="Select an EPUB file",
            initialdir=Path.home(),
            filetypes=file_types,
        )
        if file_path:
            """
            - Once here, call the epub parseing logic.
            - Add new book to the library
            """
            print(file_path)
