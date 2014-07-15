import argparse
import sys
from define import cached_key
from define import cached_lang
def parseArgs():
	about = open("usage", "r")
	parser = argparse.ArgumentParser(description=about.read())
	parser.add_argument('-s' ,
						'--source-code' , 
						dest='source' , 
						metavar = 'source code' , 
						type=argparse.FileType('r') , 
						required=True ,
						help='source-code file')
	parser.add_argument('-i' , 
						'--input-tests' ,
						dest='input' , 
						nargs='*' ,
						default=[sys.stdin] , 
						type=argparse.FileType('r') , 
						help='test-cases file')
	parser.add_argument('-o', 
						'--output-file' , 
						dest='output' , 
						default=sys.stdout , 
						type=argparse.FileType('w') , 
						help='Output file')
	parser.add_argument('-l' , 
						'--lang' , 
						dest='lang' , 
						default=cached_lang ,
						type=int ,
						help='Output file')
	parser.add_argument('--api-key' ,
						dest='api' ,
						default=cached_key ,#TODO: load the api key from a default file
						help='Output file')
	args = parser.parse_args()
	if args.api != cached_key:
		with open("src/.cached_api", "w") as f:
			f.write(args.api)
	if args.lang != cached_lang:
		with open("src/.cached_lang", "w") as f:
			f.write( str(args.lang) )
	return args