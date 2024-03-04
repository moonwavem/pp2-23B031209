import re

string = 'cdfdabbs'

x = re.search("ab*", string)
if x:
    print("Match:", x.group())
else:
    print("No match")

