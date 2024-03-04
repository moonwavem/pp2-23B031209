import re

string ="Amantay.;Aktolkyn55"

x = re.findall("[A-z][a-z]+", string)
if x: print("match:", x)
else: print ("No match")