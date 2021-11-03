#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-02
Purpose: FASTA Interleaved Paired Read Splitter
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='split interleaved FASTA sequence files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='A positional argument')

    parser.add_argument('-o',
                        '--outdir',
                        help='A named string argument',
                        metavar='DIR',
                        type=str,
                        default='split')

    args = parser.parse_args()

    check_dir = os.path.join(os.getcwd(), args.outdir)
    if not os.path.isdir(check_dir):
        os.mkdir(check_dir)

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
