import argparse
import sys
import re
from collections import Counter


def clear_file_content(file_content):
    file_content = file_content.lower()

    content_matches = re.findall(r'[^A-Za-z]+', file_content)

    if content_matches:
        return content_matches[0]
    else:
        return ''


def create_words_list(file_content):
    file_content = clear_file_content(file_content)
    return file_content.split()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Path to file with text data')
    parser.add_argument('--qty', help='Frequent words list size',
                        type=int, default=10)
    return parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath) as file:
            content = file.read()

        return content
    except (FileNotFoundError, TypeError, UnicodeDecodeError):
        return None


def get_most_frequent_words(words_list, most_common_qty):
    return Counter(words_list).most_common(most_common_qty)


if __name__ == '__main__':
    args = parse_args()

    filepath = args.file
    file_content = load_data(filepath)

    if file_content is None:
        sys.exit('Failed to open text file (not found or incorrect format)')

    words_list = create_words_list(file_content)

    words_stats = get_most_frequent_words(words_list, args.qty)

    for value, count in words_stats:
        print('{} - {}'.format(value, count))
