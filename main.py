from stats import count_words,count_character

def get_book_text(file_path):
    content=None
    with open(file_path) as f:
        content = f.read()

    return content


def main():
    book_content=get_book_text("./books/frankenstein.txt")
    number_words=count_words(book_content)
    print(f'Found {number_words} total words')
    number_characters=count_character(book_content)
    print(number_characters)
main()