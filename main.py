
from typing import Counter


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
main()

def count_words():
    book_string  = main()
    words = book_string.split()
    word_count = 0
    for word in words:
        word_count+=1
    return word_count


def count_characters():
    book_string = main()
    character_dict = {}
    lower_book_string = book_string.lower()
    characters = "abcdefghijklmnopqrstuvwxyz "
    character_count = 0
    for main_character in characters:
        count = Counter(lower_book_string)
        character_count = count[main_character]
        character_dict.update({main_character : character_count})

    return character_dict

def output():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"---{count_words()} words were found in the douument---")
    my_dict = count_characters()
    sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    del sorted_items[0]
    for key,value in sorted_items:
         print(f"The '{key}' character is found '{value}' times")

    print("--- End report ---")


output()
