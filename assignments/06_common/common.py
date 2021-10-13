#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-10-11
Purpose: Find common words
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file 1')
   
    parser.add_argument('FILE2',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file 2')
  
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='<_io.TextIOWrapper name=‘<stdout>’ mode=‘w’ encoding=‘utf-8’>'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
