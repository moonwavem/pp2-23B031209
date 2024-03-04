import re

string = "ahvhfvjfghbihfuf"

x = re.search("a.*b$",string)
if x: print("sequence:", x.group())
else: print ("Not match")