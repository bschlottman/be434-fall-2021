#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='Number of bottles to drink',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()
    
    # verses = []
    # for number in range(args.number, 0, -1):
    #     verses.append(verse(number))
    
    verses = map(verse, range(args.number, 0, -1))

    print('\n\n'.join(verses))


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    if bottle == 1:
        return '\n'.join([
            '1 bottle of beer on the wall,', '1 bottle of beer,',
            'Take one down, pass it around,',
            'No more bottles of beer on the wall!'
        ])
    else:
        text = 'bottle' if bottle == 2 else 'bottles'
        return 'n'.join([
            f'{bottle} bottle of beer on the wall,'
            f'{bottle} bottle of beer,', 'Take one down, pass it around,'
            f'{bottle - 1} bottles of beer on the wall! '
        ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
