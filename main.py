def main():
    with open('books/frankenstein.txt') as f:
        book_contents = f.read()
        number_words = script_words(book_contents)
        char_number = character_count(book_contents)
        print('Begin report of the book frankenstein.txt\n')
        print(f'The book Frankenstein has a total of {number_words} words\n')
        for char in char_number:
            print(f'The character {char} was used a total of {char_number[char]} times')
        print('\nEnd report')

def script_words(script):
    divided_script = script.split()
    number_words = len(divided_script)
    return number_words

def character_count(text):
    char_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                  'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
    return char_count

main()
