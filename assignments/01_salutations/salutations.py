#!/usr/bin/env python3
"""
Author : lillymoore <lillymoore@localhost>
Date   : 2021-09-13
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')
                        
    parser.add_argument('-n',
                        '--name',
                        help='A name to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='A flag to terminate the greeting with an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    bang = '!' if args.excited else '.'

    print('{}, {}{}'.format(args.greeting, args.name, bang))



# --------------------------------------------------
if __name__ == '__main__':
    main()
