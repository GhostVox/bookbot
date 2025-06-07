# BookBot - Text Analysis Tool

BookBot is a Python-based text analysis tool that generates detailed reports about books and other text files. This project was created as part of the [Boot.dev](https://www.boot.dev) curriculum and demonstrates fundamental Python programming concepts including file handling, string manipulation, and data processing.

## What BookBot Does

BookBot analyzes text files and provides:

- **Word count**: Total number of words in the document
- **Character frequency analysis**: Counts how many times each alphabetic character appears (case-insensitive)
- **Sorted report**: Characters ranked by frequency from most to least common

## Sample Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document
The 'e' was found 46043 times
The 't' was found 30365 times
The 'a' was found 26743 times
...
```

## Prerequisites & Installation

### Required Software

- **Python 3.x** - Download from [python.org](https://python.org)
  - Verify installation: `python --version` or `python3 --version`
- **Text editor or IDE** (optional but recommended)
  - VS Code, PyCharm, or any preferred editor

### No Additional Dependencies

BookBot uses only Python's built-in libraries, so no pip installations are required!

## Getting Started

### 1. Clone or Download the Repository

```bash
git clone [your-repo-url]
cd bookbot
```

### 2. Prepare Your Text Files

- Create a `books/` directory in the project root
- Add your text files (like `frankenstein.txt`) to the `books/` folder
- The Gutenberg project has free books that you can use to try this project out [gutenberg](https://www.gutenberg.org/ "The gutenberg project")
- The `.gitignore` file already excludes the `books/` directory from version control

### 3. Run BookBot

```bash
python main.py path_to_book
```

## Customization

To analyze different books, add the book to your books directory and include the path to the book:

```bash
python main.py books/frankenstein.txt
```

## Project Structure

```
bookbot/
├── main.py          # Main application code
├── README.md        # Project overview
├── .gitignore       # Git ignore rules
└── books/           # Directory for text files (not tracked)
    └── frankenstein.txt  # Example text file
```

## Learning Objectives

This project demonstrates:

- File I/O operations in Python
- String manipulation and processing
- Dictionary usage for counting
- List comprehensions and sorting
- Function organization and code structure
- Basic error handling concepts

Perfect for Python beginners looking to practice fundamental programming concepts with a practical, engaging project!
