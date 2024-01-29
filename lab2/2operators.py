#1
print(10 + 5)
#2
x = 5
y = 3

print(x + y)
x = 5
y = 7
x + y	
x - y	
x * y	
x / y	
x % y	
x ** y	
x // y
#3
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if 
#they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this 
#comparison returns True because x is equal to y

#4
x = 5
print(x > 3 and x < 10) #true
print(x > 3 or x < 4) #true
print(not(x > 3 and x < 10)) #false

#5
x = 5
y = 3
print(x == y) #false
print(x >= y) #true

#6 Python Membership Operators
x = ["apple", "banana"]
print("banana" in x) #true
print("pineapple" not in x) #true

#7 Python Bitwise Operators

print(6 & 3) #2
print(6 | 3) #7
print(6 ^ 3) #5

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#8 Operator Precedence
print((6 + 3) - (6 + 3)) #0
print(100 + 5 * 3) #115
print(5 + 4 - 7 + 3) #5

