#!/usr/bin/python3

import random

COMMON_CONSONANTS = [
    'b',
    'c',
    'd',
    'f',
    'k',
    'l',
    'm',
    'n',
    'p',
    'r',
    's',
    't',
    'sh',
    'ch',
]

CONSONANTS = [
    'b',
    'c',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l',
    'm',
    'n',
    'p',
    'q',
    'r',
    's',
    't',
    'v',
    'w',
    'x',
    'y',
    'z',
    'ph',
    'sh',
    'ch',
]

PREFIX_CONSTANTS = [
    'dj',
    'kn',
]

SUFFIX_CONSONANTS = [
    'ck',
]

VOWELS = [
    'a',
    'e',
    'i',
    'o',
    'u',
]

DIPTHONGS = [
    'oo',
    'ou',
    'ie',
    'oy',
    'ae',
    'iou',
    'oi',
    'ao',
    'uo',
]

SUFFIX_VOWELS = [
    'y',
]


def gen_username():
    r = random.SystemRandom()
    username = r.choice(10 * COMMON_CONSONANTS + PREFIX_CONSTANTS + CONSONANTS)
    for i in range(2):
        username += r.choice(10 * VOWELS + DIPTHONGS)
        username += r.choice(10 * COMMON_CONSONANTS + CONSONANTS +
                             SUFFIX_CONSONANTS)
        username += r.choice(10 * COMMON_CONSONANTS + CONSONANTS +
                             SUFFIX_CONSONANTS + 200 * [''])
    username += r.choice(VOWELS + SUFFIX_VOWELS)
    return username


def main():
    for i in range(10):
        print(gen_username())


if __name__ == '__main__':
    main()
