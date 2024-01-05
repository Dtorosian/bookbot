def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)

    word_count = count_words(text)
    character_count = count_characters(text)
    sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    

    print('--- Begin report on the book of Frankestein ---')
    print (f'A total of {word_count} words were found')
    for char,count in sorted_characters:
        print (f'The character "{char}" was found {count} times')
    print('--- End report ---')



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters_count = {}

    for char in text:
        if char.isalpha():
            if char in characters_count:
                characters_count[char] += 1
            else:
                characters_count[char] = 1


    return characters_count





main()