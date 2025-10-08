from stats import count_words, count_letters, sorted_hist
import sys


def get_book_text(file_path: str):
    with open(file_path) as f:
        return f.read()


def main():
    if (len(sys.argv) < 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    num_words = count_words(content)
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')

    hist = sorted_hist(count_letters(content))
    print('--------- Character Count -------')
    for v in hist:
        if (v['char'].isalpha()):
            print(f'{v['char']}: {v['num']}')


main()
