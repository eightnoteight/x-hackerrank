import os
def status_error( whatisthis, soyouare ):
	if whatisthis == 400:
		print ( '[x-hackerrank] uh oh, i made a bad request(400) this is\n'
				'               actually rare. but as this insane error occured \n'
				'               please kick this fool(eightnoteight) through his\n'
				'               e-mail id -- mr.eightnoteight [at] gmail [dot] com\n'
				'               and if you have a little more time raise an issue\n'
				'               at https::/eightnoteight.github.com/x-hackerrank\n')
		os._exit(1)
	print ('[x-hackerrank] i don\'t even have a slightest idea about how this \n'
		  '               happened. but it has happened! so please raise an issue \n'
		  '               at  https::/eightnoteight.github.com/x-hackerrank \n'
		  '[x-hackerrank] ' ), whatisthis, ' (', soyouare, ')'
	os._exit(1)