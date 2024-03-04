
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

  
import re
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)


import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")


import re 

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re 
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)


import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

import re

txt = "hello  planet"
x = re.findall("he.{2}o", txt)
print(x)