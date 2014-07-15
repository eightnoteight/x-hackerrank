#!/usr/bin/env python
import colorama
import requests
import json
from define import *
from parseArgs import *
from status_error import *
from kick_everyone import *
from parse_json import *
def main():
	url = 'http://api.hackerrank.com/checker/submission.json'
	args = parseArgs()
	#Build url
	testcases = '['
	for x in xrange(0,len(args.input)-1):
		testcases = testcases + json.dumps(args.input.pop(0).read()) +', '
	testcases = testcases + json.dumps(args.input.pop(0).read()) + ']'
	params = {
				'source' 	: args.source.read() ,
				'lang'		: args.lang ,
				'testcases'	: testcases,
				'api_key'	: args.api ,
				'wait'		: 1 ,
				'format'	: 0
			 }
	#POST url with parameters
	try:
		resp = requests.post(url, params)
	except requests.exceptions.RequestException or ConnectionError or HTTPError or TooManyRedirects or Timeout as e:
		print '[x-hackerrank] ',e
		os._exit(1)
	#post request error handling
	if resp.status_code != 200:
		status_error(resp.status_code, resp.reason)	# not this one! shoo shoo python, you musn't reach here
	json_output = resp.json()
	# 'still there may be some errors, comeback during the testing period'





	each_output = parse_json(json_output)
	kick_everyone(each_output)# I love this function






	for x in xrange(0,len(each_output)):
		print 'a'