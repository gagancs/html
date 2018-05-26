#!/usr/bin/python2

import cgi, cgitb
cgitb.enable()
import commands
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()
firefox=data.getvalue('f')
VLC=data.getvalue('v')
web_cam=data.getvalue('w')

print firefox
print VLC
print web_cam

if firefox == "firefox" :
	print commands.getoutput('sudo yum install firefox -y')
elif VLC == 'VLC' :
	print commands.getoutput('sudo yum install VLC -y')
elif webcam == 'web_cam' :
	print commands.getoutput('sudo yum install webcam -y')
