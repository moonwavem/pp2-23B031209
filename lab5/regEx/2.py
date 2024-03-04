import re

string = 'cdabbbs'

x = re.search(r"ab{2,3}",string)
if x:print("Match:", x.group())
else:print ("No match")