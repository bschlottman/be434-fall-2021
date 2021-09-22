#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-09-19
Purpose: shmound of shmoozic syllabilllllllz
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('Solfege',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a ski noise here"""

    args = get_args()
    Solfege = args.Solfege
    syl = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Derp': 'I forgot the woooords',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'}
    for word in Solfege:
        if word in syl:
            print('{}, {}'.format(word, syl.get(word)))
        else:
            print('I don\'t know "{}"'.format(word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
