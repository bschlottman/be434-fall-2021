#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-09-13
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='int',
                        nargs='+',
                        type=int,
                        help='Numbers to add')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()
    nums = args.number

    line = ''
    if len(nums) == 1:
        line = str(nums[0])
    else:
        string_ints = [str(int) for int in nums]
        line = ' + '.join(string_ints)

    print('{} = {}'.format(line,str(sum(nums))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
