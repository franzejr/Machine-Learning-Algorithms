#!/usr/bin/python 
#Handler the HTTP requests
#Filename: handler.py
# @franzejr

import cgi
import simplejson as json
import sys
sys.path.append("../methods/")
import linear_regression as lr
import loess as loess

print "Content-type: application/json\n\n"

form = cgi.FieldStorage()

data = form.getvalue("data")
method = form.getvalue("method")

if method == "linear_regression.py":
	pass
elif method == "loess.py":
	pass

vector = [3,32,4,53,234,3243,423]
print json.dumps(vector)
