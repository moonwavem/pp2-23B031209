import re

txt = "my_variable"
x = re.sub("_", "", txt)
x = re.sub("([a-z])", lambda match: match.group(1).upper(), x)
print(x)

