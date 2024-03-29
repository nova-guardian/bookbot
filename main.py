def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = get_character_counts(text)
    print(f"{num_words} words found in the document")
    print(f"The character counts are {character_counts}")


# my attempt
def get_character_counts(text):
    chr_counts = {}
    characters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
    for chr in characters:
        chr_counts[chr] = 0
        for letter in text.lower():
            if letter == chr:
                chr_counts[chr] += 1
    return chr_counts

# sample solution
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
