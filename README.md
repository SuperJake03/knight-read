# Knight Read

A simple epub reader built with Python and tkinter.

## Features

- Upload and parse epub files
- Browse your uploaded books in a library view
- Read chapter content in a dedicated reader window
- Navigate chapters via a scrollable table of contents
- Cross-platform mouse scroll support (Windows, MacOS, Linux)

## Requirements

- Python 3.12+
- tkinter (included with most Python installations)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SuperJake03/knight-read.git
cd knight-read
```

### 2. Create and activate a virtual environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate on Linux/MacOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running

```bash
python3 src/main.py
```

## Usage

1. Click **Select a file** to upload an epub
2. The book title appears in the library — click it to open the reader
3. Use the table of contents on the left to navigate chapters
4. Scroll through chapter content on the right

## Dependencies

- [ebooklib](https://github.com/aerkalov/ebooklib) — epub parsing
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing
