def kick_everyone( minions ):
	# I'm in damn love with this function. 
	# I will kill if any one touches this function.
	for x in xrange(0,len(minions)):
		print '[test-case ',x,']'
		print '----------------------------'
		tmp = minions.pop(0)
		print ''
		if tmp['stderr']:
			print '[stderr]'
			print tmp['stderr']
			print ''
		print '[memory_usage]     <->      [time]'
		print '      ', tmp['memory_usage'] , '\t\t' , tmp['time']
		print ''
		print '[stdout]'
		print tmp['stdout']
		print ''
		print '[signal]'
		print tmp['signal']