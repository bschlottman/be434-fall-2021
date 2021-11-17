#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-15
Purpose: Compress strings of DNA using Run-Length Encoding (RLE)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='a sequence to encode or a file')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Create RLE"""
    newstr = seq[0]
    initial_val = 1

    for index, char in enumerate(seq[1:]):
        if char == newstr[-1]:
            initial_val += 1
            if index == len(seq) - 2:
                newstr += str(initial_val)

        elif char != newstr[-1]:
            if initial_val != 1:
                newstr += str(initial_val)
            newstr += char
            initial_val = 1

    return newstr


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
def main():
    """shmake a shmazz shmoise shmere"""

    args = get_args()
    if os.path.isfile(args.text):
        with open(args.text, encoding='UTF-8') as dna_file:
            for seq in dna_file.read().splitlines():
                print(rle(seq))
    else:
        print(rle(args.text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
