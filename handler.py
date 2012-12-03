#!/usr/bin/python 
#Handler the HTTP requests
#Filename: handler.py
# @franzejr

import cgi

form = cgi.FieldStorage()

method = form.getvalue("method")

if method == "loess":
	pass
elif method == "linear_regression":
	pass
