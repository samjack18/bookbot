#!/usr/bin/env python3

def get_num_words (text):
    return len(text.split())

def count_letters (text):
    
    letter_counts = {}
    
    for char in text:
        char = char.lower()

        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts

def sort_dict_by_values (unsorted_dict):
    sorted_values = list(unsorted_dict.items())
    sorted_values.sort(key=lambda item: item[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_values}
    return sorted_dict
