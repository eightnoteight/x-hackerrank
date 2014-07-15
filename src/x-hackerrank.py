#!/usr/bin/env python
import argparse
import sys
import colorama
import requests
import json
url = 'POST http://api.hackerrank.com/checker/submission.json'
about = open("../usage", "r")
parser = argparse.ArgumentParser(description=about.read())
parser.add_argument('-s',
					'--source-code', 
					dest='source', 
					metavar = 'sourutce code', 
					type=argparse.FileType('r'), 
					help='source-code file')
parser.add_argument('-i', 
					'--input-tests',
					dest='input', 
					default=sys.stdin, 
					type=argparse.FileType('r'), 
					help='test-cases file')
parser.add_argument('-o', 
					'--output-file', 
					dest='output', 
					default=sys.stdout, 
					type=argparse.FileType('w'), 
					help='Output file')
args = parser.parse_args()

args.output.close()
args.input.close()
args.source.close()