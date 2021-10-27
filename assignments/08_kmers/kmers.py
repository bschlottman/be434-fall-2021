#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='input Files to compare')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='input Files to compare')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default='3')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)

# --------------------------------------------------
if __name__ == '__main__':
    main()
