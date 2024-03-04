#1
ans:['apple', 'banana', 'cherry']
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2Списки допускают дублирование значений:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #3

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
 #3 Список может содержать разные типы данных:
list1 = ["abc", 34, True, 40, "male"]

#3,5 What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#<class 'list'> 

#4 Конструктор списка()
#Также можно использовать конструктор list() при создании нового списка.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) 
#['apple', 'banana', 'cherry']

#5
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#6 Изменить значение элемента
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

#7
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#8
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 
#['apple', 'blackcurrant', 'watermelon', 'cherry']

#9
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

#10
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
#['apple', 'banana', 'watermelon', 'cherry']

#11 To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']

#11
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#12
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
#['apple', 'banana', 'watermelon', 'cherry']

#13
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']
'''The extend() method does not have to append lists, you 
can add any iterable object (tuples, sets, dictionaries etc.).'''

#14
thislist = ["apple","banana"]
thislist.remove("apple")
print(thislist)

#15 pop-remove by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) 
#['apple', 'cherry']

#16
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']

#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

#17
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# []

#18
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
""" apple
    banana
    cherry
"""

thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
  print(thislist[i])


i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
 #short
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#19
fruits = ["apple","banana","orange","anans"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print (newlist)
#short
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)