#!/usr/bin/python2

import cgi, cgitb
cgitb.enable()
import commands
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()
name=data.getvalue('n')
email=data.getvalue('e')
password=data.getvalue('p')
contact=data.getvalue('c')


print name
print email
print password
print contact
