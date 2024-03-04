import re

string ="AmantayaktolkyТ55"

x = re.findall("[a-z]+", string)
print("res:", x)