import urllib, json, sys, os

if (len(sys.argv) < 2): 
	print('Please specify at least one list of druids as input')
	quit()

print sys.argv[1]
print len(sys.argv)
