#!/usr/bin/python2

import cgi

print "content-type:text/html"
print ""

web_data=cgi.FieldStorage()
out=web_data.getvalue('x')

print out

