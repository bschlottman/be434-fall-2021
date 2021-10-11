#!/usr/bin/env python3
"""
Author : bschlottmam <bschlottman@email.arizona.edu>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence', metavar='str', help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()

    codon_table = {}
    for line in args.codons:
        key, value = line.rstrip().split()
        codon_table[key] = value

    k = 3
    seq = args.sequence.upper()
    protein = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        protein += codon_table.get(codon, '-')
    #     print(codon_table.get(codon, '-'), end='', file=args.outfile)
    # print(file=args.outfile)
    # print(f'Output written to "{args.outfile.name}".')
    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
