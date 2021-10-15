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
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
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
    """Make a jazz noise here"""

    args = get_args()
    
    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
