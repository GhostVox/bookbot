from stats import count_words
import sys


def Main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = args[1]
    book_contents = read_book(book)
    words = count_words(book_contents)
    characters = count_characters(book_contents)
    reports = report(characters)
    sorted_report = sorted(reports, reverse=True, key=sort_on)
    print(f"--- Begin report of {book} ---")

    print(f"Found {len(words)} total words")
    print(type(sorted_report))
    for r in sorted_report:
        print(f"{r["character"]}: {r["count"]}")
    return


def read_book(book):
    with open(book) as f:
        file_contents = f.read()

        return file_contents


def count_characters(string):
    characters = {}
    lowered_string = string.lower()
    for character in lowered_string:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
        else:
            pass
    return characters


def report(dict):
    dict_of_words = []
    for c in dict:
        dict_of_words.append({"character": c, "count": dict[c]})
    return dict_of_words


def sort_on(dict):
    return dict["count"]


Main()
