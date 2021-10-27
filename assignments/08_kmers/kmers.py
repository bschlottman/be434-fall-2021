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
                        help='input File to compare',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='input File to compare',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default='3')

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()
    F1 = args.FILE1
    F2 = args.FILE2
    kmers = args.kmer

    k1 = count_kmers(F1, kmers)
    k2 = count_kmers(F2, kmers)

    commonk = sorted(list(set(k1).intersection(k2)))

    for kmers in commonk:
        print('{:10}{:6}{:6}'.format(kmers, k1.get(kmers), k2.get(kmers)),
              end='\n')


# --------------------------------------------------
def count_kmers(file, k):
    """Create a dictionary of kmers from each file"""

    mers = {}
    for line in file:
        for word in line.split():
            for kmers in find_kmers(word, k):
                if kmers in mers:
                    mers[kmers] += 1
                else:
                    mers[kmers] = 1
    return mers


# --------------------------------------------------
def find_kmers(seq, k):
    """Find kmers in a string"""

    n = len(seq) - k + 1

    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------

if __name__ == '__main__':
    main()
