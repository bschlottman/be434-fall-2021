#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-10-10
Purpose: convert vowels in a string or text file to a provided vowel
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')
    # Take a positional argument that might be some plain text
    parser.add_argument(
        '-v',
        '--vowel',
        help='The vowel to substitute',
        choices=['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'],
        metavar='str',
        type=str,
        default='a')
    # or may name a file
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    vowel_dict_low = list('aeiou')
    vowel_dict_up = vowel_dict_low.upper()
    new_text = []

    for char in text:
        if char in vowel_dict_low:
            new_text.append(vowel)
        elif char in vowel_dict_up:
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

    print(''.join(new_text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
