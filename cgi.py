#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()

time = form.getvalue('time')
mondayOff = form.getvalue('mondayOff')
majorTask = form.getvalue('majorTask')
gameOfThrones = form.getvalue('gameOfThrones')

print "Content-type: text/html"
print "<head>"
print "<title>Your Fate</title>"
print "</head>"
print "<body>"
if((time > 1000 or majorTask == "No") and gameOfThrones == "Yes" and mondayOff == "Yes"):
print " <h2> You can watch The Game Of Thrones </h2>"
else:
print " <h2> Sorry Bud, you cant watch anything because you work Monday & chores to do </h2>"

print "</body>"