#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-16
Purpose: test your memory
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        help='Initial str of length 5')
    # parser error if an initial str of length 5 is not given
    parser.error()
    return parser.parse_args()


# --------------------------------------------------
def main():
    """bring in a new random string on a new line, 
        & replace old line with | | | | |, keeping line position"""

    args = get_args()
    import random
    import string

    # printing lowercase
    letters = string.ascii_lowercase
    print ( ''.join(random.choice(letters) for i in range(10)) )
    for args.positional:
        print(args.positional) if args.positional is > str[:6]


# --------------------------------------------------
if __name__ == '__main__':
    main()
