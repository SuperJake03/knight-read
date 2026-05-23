from pathlib import Path
from tkinter import *
from tkinter import filedialog, scrolledtext, ttk

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
        self.main_frame = ttk.Frame(self.root, padding=3)
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=1)

        # All container frames
        self.welcome_frame = ttk.Frame(self.main_frame, borderwidth=5, relief="ridge")
        self.upload_frame = ttk.Frame(self.main_frame, borderwidth=5, relief="ridge")
        self.library_frame = ttk.Frame(self.main_frame, borderwidth=5, relief="ridge")

        # Layout of container frames
        self.welcome_frame.grid(column=0, row=0, sticky=(W, E))
        self.upload_frame.grid(column=0, row=1, sticky=(W, E))
        self.library_frame.grid(column=0, row=2, sticky=(N, W, E, S))

        # Welcome frame widgets
        welcomelabel = ttk.Label(self.welcome_frame, text="Welcome to Knight Read!")
        welcomelabel.grid(column=0, row=0, pady=20)
        self.welcome_frame.columnconfigure(0, weight=1)

        # Upload frame widgets
        uploadlabel = ttk.Label(self.upload_frame, text="Upload new EPUB here!")
        uploadbutton = ttk.Button(
            self.upload_frame, text="Select a file", command=self.upload_file
        )

        # Layout of upload frame widgets
        uploadlabel.grid(column=0, row=0, pady=5)
        uploadbutton.grid(column=0, row=1, pady=5)
        self.upload_frame.columnconfigure(0, weight=1)

        # library frame widgets
        librarylabel = ttk.Label(self.library_frame, text="Library")
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
            book_button = ttk.Button(
                self.library_frame,
                text=new_book.title,
                command=lambda b=new_book: self.display_book(b),
            )
            book_button.pack()

    def display_book(self, book):
        reader_window = Toplevel()
        reader_window.title(book.title)
        reader_frame = ttk.Frame(reader_window, padding=3)
        reader_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        content_area = scrolledtext.ScrolledText(
            reader_frame, font=("Times New Roman", 15)
        )
        content_area.grid()

        content_area.insert(INSERT, book.chapters[3].content)

        content_area.config(state="disabled")
