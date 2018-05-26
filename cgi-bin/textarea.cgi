#!/usr/bin/python2

import cgi, cgitb
cgitb.enable()
import commands
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()
name=data.getvalue('t')

print name


