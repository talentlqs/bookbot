from stats import get_book_text
from stats import count_words
from stats import char_dict
from stats import print_report
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]#"books/frankenstein.txt"
    frankenstein = get_book_text(path)
    words_in_book = count_words(frankenstein)
    dict = char_dict(frankenstein)
    print(f"{words_in_book} words found in the document")
    print(char_dict(frankenstein))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_book} total words")
    print("--------- Character Count -------")
    
    print_report(dict)
    
    
    print("============= END ===============")


main()