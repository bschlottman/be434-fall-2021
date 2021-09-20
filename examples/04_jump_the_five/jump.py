#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-09-20
Purpose: obfuscate numerical text
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Trick da feds',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Jump the Five')
    
    return parser.parse_args()

    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    for char in args.text:
        # if char in jumper:
        #     print(jumper[char], end='')
        # else:
        #     print(char, end='')
        print(jumper.get(char, char), end='')

    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
