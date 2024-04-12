chars_dict = {'a': 26743, 'b': 5026, 'c': 9243, 'd': 16863}

def sort_on(dict):
    return dict["num"]

sorted_chars = []
for chr in chars_dict:
    character_numbers = {"chr": chr, "num": chars_dict[chr]}
    sorted_chars.append(character_numbers)

sorted_chars.sort(reverse=True, key=sort_on)

for character in sorted_chars:        
    print(f"The '{character["chr"]}' character was found {character["num"]} times")

    # This is a test line


    
    
    
