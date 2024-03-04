#1
print(10 > 9) #TRUE
print(10 == 9) #FALSE
print(10 < 9) #False
#2
a = 200
b = 33
if b > a:
  print("b is greater than a") 
else:
  print("b is not greater than a")
# b is not greater than a
#3
print(bool("Hello"))
print(bool(15))
#4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#5 The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#6 The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#7 __len__
class myclass():
  def __len__(self):
    return 0
  
myobj = myclass()
print(bool(myobj))
#FAlSE
#8
def myFunction() :
  return True

print(myFunction())
#True
#9
def myFunction():
  return True
if myFunction():
  print("YES!")
else:
  print ("NO!")
#YES
#10
"""Python также имеет множество встроенных функций, которые возвращают логическое значение, 
например функцию isinstance() , которую можно использовать для определения того, 
принадлежит ли объект к определенному типу данных"""

x = 200
print(isinstance(x, int))
#TRUE

