#!/usr/bin/env python3
from config import PATH_TO_BOOK
from stats import get_num_words

def get_book_text (path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        read_data = f.read()
    return read_data

def main ():
    path_to_book = PATH_TO_BOOK
    book_text = get_book_text(path_to_book)
    words = get_num_words(book_text)
    print(f"{words} words found in the document")

main()