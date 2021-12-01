#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-12-01
Purpose: finish BE534
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python clone of tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)
    args = parser.parse_args()

    if args.files != argparse.FileType('rt', encoding='UTF-8'):
        parser.error(f"can't open {args.files}")
    else:
        return args # not sure this is the right way... need to figure out how to read in the input file...
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
