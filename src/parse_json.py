import os
def parse_json( data ):

	allminions = []
	data = data['result'] # this is known as wriggiling, but I want to know it's cost.
	try:
		if data['compilemessage'] == '':
			raise TypeError
		print data['compilemessage']
		print '\n\n[x-hackerrank] oh boy! compilation error! every you get a compilation error'
		print 	  '               from me, some where in the galaxy a star dies !'
		os._exit(0)
		
	except TypeError:
		for x in xrange(0,len(data['censored_stderr'])):
			allminions.append({
								"memory_usage"	: data["memory"].pop(0),
								"message"		: data["message"].pop(0),
								"signal"		: data["signal"].pop(0),
								"stderr"		: data["stderr"].pop(0),
								"stdout"		: data["stdout"].pop(0),
								"time"			: data["time"].pop(0)
				})
	return allminions
