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
        welcome_label = ttk.Label(self.welcome_frame, text="Welcome to Knight Read!")
        welcome_label.grid(column=0, row=0, pady=20)
        self.welcome_frame.columnconfigure(0, weight=1)

        # Upload frame widgets
        upload_label = ttk.Label(self.upload_frame, text="Upload new EPUB here!")
        upload_button = ttk.Button(
            self.upload_frame, text="Select a file", command=self.upload_file
        )

        # Layout of upload frame widgets
        upload_label.grid(column=0, row=0, pady=5)
        upload_button.grid(column=0, row=1, pady=5)
        self.upload_frame.columnconfigure(0, weight=1)

        # library frame widgets
        library_label = ttk.Label(self.library_frame, text="Library")
        library_label.pack(side="top")

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

            # Add book to library, button
            book_button = ttk.Button(
                self.library_frame,
                text=new_book.title,
                command=lambda b=new_book: self.display_book(b),
            )
            book_button.pack()

    def display_book(self, book):
        # reader window
        reader_window = Toplevel()
        reader_window.title(book.title)
        reader_window.columnconfigure(0, weight=1)
        reader_window.rowconfigure(0, weight=1)

        # reader main frame
        reader_frame = ttk.Frame(reader_window, padding=3)
        reader_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        reader_frame.columnconfigure(0, weight=1)
        reader_frame.columnconfigure(1, weight=1)

        # scrollable TOC frame on left
        toc_container = ttk.Frame(reader_frame)
        toc_container.grid(column=0, row=0, sticky=(N, W, S))

        canvas = Canvas(toc_container)
        canvas.grid(column=0, row=0, sticky=(N, W, S))

        scrollbar = ttk.Scrollbar(
            toc_container, orient="vertical", command=canvas.yview
        )
        scrollbar.grid(column=1, row=0, sticky=(N, S))

        toc_frame = ttk.Frame(canvas)
        toc_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=toc_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Scrolled text to display chapter content on right
        content_area = scrolledtext.ScrolledText(
            reader_frame, font=("Times New Roman", 15)
        )
        content_area.grid(column=1, row=0, sticky=(N, S, E))

        # Add chapter buttons to TOC frame
        row = 0
        for chap in book.chapters:
            chap_button = ttk.Button(
                toc_frame,
                text=chap.title,
                command=lambda content=content_area, c=chap: self.change_chapter(
                    content, c
                ),
            )
            chap_button.grid(column=0, row=row)
            row += 1

        # Display first chapter by default
        content_area.insert("1.0", book.chapters[0].content)
        content_area.config(state="disabled")

    def change_chapter(self, content_area, chapter):
        content_area.config(state="normal")
        content_area.delete("1.0", END)
        content_area.insert("1.0", chapter.content)
        content_area.config(state="disabled")
