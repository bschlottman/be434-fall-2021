#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-07
Purpose: Find the conserved bases in two or more aligned sequences
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('alignments',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file',
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def compare_chars(lines, line_num, position):
    """"Compare each character in the aligned sequences"""

    same_letters = {}
    for letter in range(position):
        compare = [lines[line][letter] for line in range(line_num)]
        if len(set(compare)) != 1:
            same_letters[letter] = 'X'
        else:
            same_letters[letter] = '|'

    return same_letters


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()

    line_list = [line.rstrip() for line in args.alignments]
    line_num = len(line_list)
    position = len(line_list[0])

    pos_match = compare_chars(line_list, line_num, position)

    for lines in line_list:
        print(lines.rstrip())

    for pos in range(position):
        print(pos_match[pos], end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
