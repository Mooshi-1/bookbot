def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    print(f"{num_words} words found in the document")

#pull book
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count number of words
def count(string):
    words = string.split()
    return len(words)
    
main()