#!/usr/bin/python
import commands

cmd_list = [
	'lib/wnf.py --pull origin master',
	'lib/wnf.py -l',
	'lib/wnf.py --sync_all'
]
err = 0
for cmd in cmd_list:
	stat, op = commands.getstatusoutput(cmd)
	if stat != 0:
		print "something went wrong"
		print "cannot proceed with update"
		print "status: %s" % stat
		print "output: %s" % op
		err = 1
		break
		
if not err:
	print "update_erpnext.py --> run success."
else:
	print "update_erpnext.py --> run failed."