import re

txt = "MyVariable"
x = re.sub("_", "", txt)
x = re.sub("([A-Z])", lambda match: match.group(1).lower(), x)
print(x)
