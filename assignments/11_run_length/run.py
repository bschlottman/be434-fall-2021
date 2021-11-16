#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-15
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='a sequence to encode or a file')

    args = parser.parse_args()

    if os.path.isfile(args.sequence):
        args.sequence = open(args.sequence).read().rstrip()

    return args


# --------------------------------------------------
def main():
    args = get_args()
    for seq in args.sequence.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    """Create RLE"""

    return ''


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()