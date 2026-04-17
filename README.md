# Knight Read
- An EPUB reader

## Next Steps
- Build book dataclasses to store parsed epub data
- Continue setting up splash page
- Work on putting widgets into place
- Text fonts and font sizes

## Things this eBook reader should do

- Take in an EPUB file from GUI
- Parse the EPUB file
- Display EPUB file content on the GUI

### Tkinter GUI
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/tutorial/index.html
https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

### parsing EPUB files
Look into Ebooklib: https://pypi.org/project/EbookLib/

## TODO

- Create a book object
  - stores epub spine
  - contents
- Create chapter object
- Create image object
- Create stylesheet object

- set up tkinter GUI splash page
  - Create welcome screen
  - Allow file input
- parse epub
- disaplay contents on GUI
  - Allow for page turning
- Add a database to store books
  - Save last page
