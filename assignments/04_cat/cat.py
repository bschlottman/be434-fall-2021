#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-09-28
Purpose: meow
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default='FALSE')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()

    # 1. The first `for` loop will iterate over the file arguments
    for fh in args.input:
        # 2. The second `for` loop will iterate over the lines in each file
        for l_num, line in enumerate(fh, start=1):
            if args.number is True:
                print("     {}\t{}".format(l_num, line), end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
