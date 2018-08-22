import argparse
import sys
from fnmatch import fnmatch
import re


def clear_word(word):
    word = word.strip().lower()
    return re.sub('[:\.\?,!"\'<>]+', '', word)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Path to file with text data')
    return parser.parse_args()


def load_data(filepath):
    try:
        if not fnmatch(filepath, '*.txt'):
            raise TypeError

        with open(filepath) as file:
            content = file.read().splitlines()
    except (FileNotFoundError, TypeError):
        return None

    words_list = []

    for line in content:
        words = line.split()

    for word in words:
        word = clear_word(word)
        words_list.append(word)

    return words_list


def get_most_frequent_words(words_list):
    words_stats = {}

    for word in words_list:
        if word not in words_stats:
            count = 1
        else:
            count = words_stats[word] + 1

        words_stats[word] = count

    stats_data = []

    sorted_data = sorted(words_stats, key=words_stats.get, reverse=True)

    for word in sorted_data[:10]:
        stats_data.append((word, words_stats[word]))

    return stats_data


if __name__ == '__main__':
    args = parse_args()

    filepath = args.file
    words_list = load_data(filepath)

    if words_list is None:
        sys.exit('Failed to open text file (not found or incorrect format)')

    words_stats = get_most_frequent_words(words_list)

    for word in words_stats:
        word_value, word_count = word
        print('%s - %s' % (word_value, word_count))
