def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = count_characters(text)
    report = compile_report(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words founr in the document.")
    print(report)


#pull book
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count number of words
def count_words(string):
    words = string.split()
    return len(words)
    
def count_characters(string):
    alphabet = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    lowercase = string.lower() #convert to lowercase
    for characters in lowercase:
        if characters in alphabet:
            alphabet[characters] += 1
    #print(alphabet)
    return(alphabet)

def compile_report(num_letters):
    return num_letters


        

main()