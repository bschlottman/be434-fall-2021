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
                        help='input Files to compare',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='input Files to compare',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmers',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default='3')

    args = parser.parse_args()

    if args.kmers < 1:
        parser.error(f'--kmers "{args.kmers}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    F1 = args.FILE1
    F2 = args.FILE2
    kmers = args.kmers

    k1 = count_kmers(F1, kmers)
    k2 = count_kmers(F2, kmers)

    commonk = sorted(list(set(k1).intersection(k2)))

    for kmers in commonk:
        print('{:10} {:6} {:6}'.format(kmers, k1.get(kmers), k2.get(kmers)),
              end = '\n')


# --------------------------------------------------
def count_kmers(file, k):
    """Create a dictionary of kmers in each file"""
    
    mers = {}
    for line in file:
        for word in line.split():
            for kmers in find_kmers(word, k):
                if kmers in mers:
                    words[kmers] += 1
                else:
                    words[kmers] = 1
    return mers


# --------------------------------------------------
def find_kmers(seq, k):
    """Find kmers in a string"""

    n = len(seq) - k + 1

    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
