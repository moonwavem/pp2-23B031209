x = 5
y = "John"
print(x)
print(y)

x = 4    
x = "Sally"
print(x)

x = int(3)
y = float(3)
z = str(3)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
#SAME
x = 'John'

a = 4
A = "Sally"

#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:

"""n myvar = "John"
my-var = "John"
my var = "John" """

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#wrong 
x = 5
y = "John"
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"
def myFunc():
    print("python is "+x)
myFunc()

#global
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)