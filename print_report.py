def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars_dict(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")
    for character in sorted_chars:        
        print(f"The '{character["chr"]}' character was found {character["num"]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def sort_chars_dict(chars_dict):
    sorted_chars = []
    for chr in chars_dict:
        character_numbers = {"chr": chr, "num": chars_dict[chr]}
        sorted_chars.append(character_numbers)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()