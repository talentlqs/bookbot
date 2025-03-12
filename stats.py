def get_book_text(filepath):
    with open(filepath) as f:
        txt = f.read()
    return txt

def count_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def char_dict(book):
    book_tmp = book.lower()
    words = book_tmp.split()
    dict = {}
    count = 0
    for char in book_tmp:
        dict[char] = dict.get(char, 0) + 1     
    return dict

def print_report(dict):
    formatted_list = [f"{key}: {value}" for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True)]
    for entry in formatted_list:
        print(entry)



