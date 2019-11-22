#!/usr/bin/env python3

from collections import Counter
import sys

def count_words(input_file):
    words = []
    with open(input_file) as f:
        for line in f:
            words.extend(line.split())

    counter = Counter(words)
    most_commons = counter.most_common(10)
    for word, count in most_commons:
        print(word, ' apperears ',  count, "times")


#if __name__ == "__main__":
try:
    input_file = sys.argv[1]
except IndexError as e:
    print("usage: python ten_words.py filename")
    raise e

count_words(input_file)
