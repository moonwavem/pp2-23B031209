import re

txt = "The rain, in Spain."
x = re.sub(r'[ ,.]', ':', txt)
print(x)
