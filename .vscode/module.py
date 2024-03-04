"""
import mymodule
mymodule.greeting("Jonathan")

import mymodule
print(mymodule.person1["age"])

import mymodule as mx
print (mx.person1["age"])

import platform
print (platform.system())

from mymodule import person1
print (person1["age"])

import mymodule

print(
dir(mymodule)
)
"""

import datetime
print(datetime.datetime.now())


import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2020,2,18)
print(x.year)


import datetime
x = datetime.datetime(2024, 1, 20)
print(x.strftime("%C"))