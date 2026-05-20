from pathlib import Path
from tkinter import *
from tkinter import filedialog, ttk

from epub_parser import book_upload


class KnightReadGUI:
    def __init__(self):
        # Library
        self.library = {}

        # Root Window
        self.root = Tk()
        self.root.title("Knight Read")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Main frame to put all other frames into.
        self.mainframe = ttk.Frame(self.root, padding=3)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(2, weight=1)

        # All container frames
        self.welcomeframe = ttk.Frame(self.mainframe, borderwidth=5, relief="ridge")
        self.uploadframe = ttk.Frame(self.mainframe, borderwidth=5, relief="ridge")
        self.libraryframe = ttk.Frame(self.mainframe, borderwidth=5, relief="ridge")

        # Layout of container frames
        self.welcomeframe.grid(column=0, row=0, sticky=(W, E))
        self.uploadframe.grid(column=0, row=1, sticky=(W, E))
        self.libraryframe.grid(column=0, row=2, sticky=(N, W, E, S))

        # Welcome frame widgets
        welcomelabel = ttk.Label(self.welcomeframe, text="Welcome to Knight Read!")
        welcomelabel.grid(column=0, row=0, pady=20)
        self.welcomeframe.columnconfigure(0, weight=1)

        # Upload frame widgets
        uploadlabel = ttk.Label(self.uploadframe, text="Upload new EPUB here!")
        uploadbutton = ttk.Button(
            self.uploadframe, text="Select a file", command=self.upload_file
        )

        # Layout of upload frame widgets
        uploadlabel.grid(column=0, row=0, pady=5)
        uploadbutton.grid(column=0, row=1, pady=5)
        self.uploadframe.columnconfigure(0, weight=1)

        # library frame widgets
        librarylabel = ttk.Label(self.libraryframe, text="Library")
        librarylabel.pack(side="top")

        self.root.mainloop()

    def upload_file(self):
        file_types = [("EPUB files", "*.epub")]
        file_path = filedialog.askopenfilename(
            title="Select an EPUB file",
            initialdir=Path.home(),
            filetypes=file_types,
        )
        if file_path:
            # Create new book object
            new_book = book_upload(file_path)
            self.library[new_book.title] = new_book
            print(f"{new_book.title} uploaded!!!")
            print(f"library now consists of: {self.library.keys()}")

            # Add book to library, button
            bookbutton = ttk.Button(
                self.libraryframe,
                text=new_book.title,
                command=lambda b=new_book: self.display_book(b),
            )
            bookbutton.pack()

    def display_book(self, book):
        print(f"This book is {book.title}")
