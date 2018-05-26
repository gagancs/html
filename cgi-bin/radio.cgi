#!/usr/bin/python2

import cgi, cgitb


import commands

cgitb.enable()
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()
name=data.getvalue('f')

print name


