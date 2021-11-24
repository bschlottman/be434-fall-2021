#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-21
Purpose: grep the Casbah
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('files',
                        metavar='Input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_files = len(args.files)

    for fh in args.files:
        for line in fh:
            if re.search(args.pattern, line, re.I if args.insensitive else 0):
                # print('{}{}'.format(f'{fh.name}:' if num_files > 1 else '',
                #                     line, end='', file=args.outfile)
                args.outfile.write('{}{}'.format(
                    f'{fh.name}:' if num_files > 1 else '', line))


# --------------------------------------------------
if __name__ == '__main__':
    main()
