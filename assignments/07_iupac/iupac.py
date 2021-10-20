#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-10-15
Purpose: Rock the Rialto
"""

import argparse
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

    for seq in args.seq:
        seq_out = ""
        regexp_out = ""

        for char in seq:
            if len(Bases.get(char)) > 1:
                seq_out = seq_out + char
                regexp_out = regexp_out + '[{}]'.format(Bases.get(char))
            else:
                seq_out = seq_out + char
                regexp_out = regexp_out + Bases.get(char)

        print('{} {}'.format(seq_out, regexp_out), file=args.outfile)
# '!=' same as 'is not'
    if args.outfile != sys.stdout:
        print('Done, see output in "{}"'.format(args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
