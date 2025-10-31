from stats import count_words,count_character,sorting_list
import sys

def get_book_text(file_path):
    content=None
    with open(file_path) as f:
        content = f.read()

    return content


def main():
    book_content=None
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content=get_book_text(sys.argv[1])
    number_words=count_words(book_content)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f'Found {number_words} total words')
    print("--------- Character Count -------")
    number_characters=count_character(book_content)
    #print(number_characters)
    sorted_list=sorting_list(number_characters)
    for character in sorted_list:
        if character["char"].isalpha():
            print(f'{character["char"]}: {character["num"]}')
    print("============= END ===============")
main()