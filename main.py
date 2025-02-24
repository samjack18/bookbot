#!/usr/bin/env python3
import sys
from stats import get_num_words, count_letters, sort_dict_by_values

def get_book_text (path_to_file):
    try:
        with open(path_to_file, encoding="utf-8") as f:
            return f.read()
    except IOError:
        print(f"Error: There was an issue reading the file at '{path_to_file}'.")
        sys.exit(1)

def main ():
    
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    words = get_num_words(book_text)
    letters = count_letters(book_text)
    sorted_letters = sort_dict_by_values(letters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_letters.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()