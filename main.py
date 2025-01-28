
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
    print(word_count)

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
    print(f"{count_words()} words found in the document...")
    my_dict = count_characters()
    for key,value in my_dict:
            print(f"The '{my_dict[key]} character was found {my_dict[value]} times.'")

        
output()


