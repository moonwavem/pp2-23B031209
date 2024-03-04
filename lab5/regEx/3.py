import re

string ="Amantay_aktolkyn_55"

x = re.findall("[a-z]+_[a-z]+", string)
if x: print("match:", x)
else: print ("No match")