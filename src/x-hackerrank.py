#!/usr/bin/env python
import argparse
import sys
import colorama
import requests
import json
from define import *
url = 'http://api.hackerrank.com/checker/submission.json'
about = open("../usage", "r")
parser = argparse.ArgumentParser(description=about.read())
parser.add_argument('-s',
					'--source-code', 
					dest='source', 
					metavar = 'source code', 
					type=argparse.FileType('r'), 
					required=True,
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
parser.add_argument('-l', 
					'--lang', 
					dest='lang', 
					default=2,
					type=int,
					help='Output file')
parser.add_argument('--api', 
					dest='api', 
					default='yourapikeyhere',#TODO: load the api key from a default file
					help='Output file')
args = parser.parse_args()
params = {
			'source' 	: args.source.read() ,
			'lang'		: args.lang ,
			'testcases'	: "[" + json.dumps(args.input.read()) + "]" ,
			'api_key'	: args.api,
			'wait'		: 1,
			'format'	: 0
		 } 
resp = requests.post(url, params)
json_output = resp.json()
stdout = json_output['result']['stdout']
for x in xrange(0,len(stdout)):
	print stdout[x]


args.output.close()
args.input.close()
args.source.close()