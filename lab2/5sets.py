thisset = {"apple", "banana", "cherry"}
print(thisset) #{'apple', 'banana', 'cherry'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'apple', 'banana', 'cherry'}

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #3

"""Значения и считаются одинаковыми значениями в 
множествах, и рассматриваются как дубликаты:True1""" 

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #{True, 2, 'banana', 'cherry', 'apple'}

"""Значения и считаются 
одинаковыми значениями в множествах, и рассматриваются как дубликаты:False0"""

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #{False, True, 'cherry', 'apple', 'banana'}

#Элементы набора могут иметь любой тип данных:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}#{True, 34, 40, 'male', 'abc'}

myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'apple', 'cherry', 'banana'}

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
"""
   banana
   apple
   cherry
"""

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#True

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#{'banana', 'orange', 'cherry', 'apple'}

#Чтобы добавить элементы из другого набора в текущий, используйте метод.update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#Объект в методе не имеет Чтобы быть множеством,
#это может быть любой итерируемый объект (кортежи, списки, словари и т.д.).update()
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
"""{'banana', 'cherry', 'apple', 'orange', 'kiwi'}"""

# чтобы удалить элемент в наборе, используйте метод , или .remove()discard()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Если удаляемый элемент не существует, возникнет ошибка.remove()

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Если удаляемый элемент не существует, ошибка НЕ возникнет.discard()

thisset = {"apple", "banana", "cherry"}
thisset.discard("bana")
print(thisset)
#{'apple', 'banana', 'cherry'}

"""Вы также можете использовать метод для удаления Но этот 
метод удалит случайный элемент, поэтому вы не можете быть уверены, 
какой элемент будет удален.pop()"""

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
"""cherry
{'apple', 'banana'}"""

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#set()

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists

"""Вы можете использовать метод, который возвращает новый набор, содержащий 
все элементы из обоих наборов, или метод, который вставляет
все элементы из одного набора в другой:union()update()"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#{'c', 1, 3, 2, 'a', 'b'}


#Метод вставляет элементы из set2 в set1:update()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

"""Метод сохранит только те 
элементы, которые присутствуют в обоих наборах.intersection_update()"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update
print(x)
#{'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)
#{'apple'}

"""Метод будет оставить только те элементы, которые НЕ присутствуют 
в обоих наборах.symmetric_difference_update()"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#{'google', 'banana', 'microsoft', 'cherry'}

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)
#{'google', 'banana', 'microsoft', 'cherry'}
