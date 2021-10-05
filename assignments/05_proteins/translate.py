#!/usr/bin/env python3
"""
Author : bschlottmam <bschlottman@email.arizona.edu>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nucleotides',
                        metavar='str',
                        nargs='*',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()
    seq = args.nucleotides
    fh_in = args.codons
    fh_out = args.outfile
    


    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
