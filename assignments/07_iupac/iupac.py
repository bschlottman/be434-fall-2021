#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-10-15
Purpose: Rock the Rialto
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line shmarguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Do a flip here"""

    args = get_args()
    sequence_list = args.seq

    Bases = {
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'T': 'T',
        'U': 'U',
        'R': 'AG',
        'Y': 'CT',
        'S': 'GC',
        'W': 'AT',
        'K': 'GT',
        'M': 'AC',
        'B': 'CGT',
        'D': 'AGT',
        'H': 'ACT',
        'V': 'ACG',
        'N': 'ACGT'
    }

    for code in sequence_list:
        outseq = ""
        outre = ""
        for char in code:
            if len(Bases.get(char)) > 1:
                outseq = outseq + char
                outre = outre + '[{}]'.format(Bases.get(char))
            else:
                outseq = outseq + char
                outre = outre + Bases.get(char)
    print('{} {}'.format(sequence_list, outseq, outre))


# --------------------------------------------------
if __name__ == '__main__':
    main()
