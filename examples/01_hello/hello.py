#!/usr/bin/env python

#Author: Bradley Schlottman, taken from Ken Yoens-Clark <bschlottman@email.arizona.edu>
# Purpose: Say hello


import argparse

def get_args():
	parser = argparse.ArgumentParser(description='Say Hello')
	parser.add_argument('-n', '--name', metavar='name',
					default='World', help='Name to greet')
	return parser.parse_args()
	
def main():
	args = get_args()
	print('Hello, ' + args.name + '!')
	
if __name__ == '__main__':
	main()
	


