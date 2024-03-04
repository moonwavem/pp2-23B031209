mytuple = ("apple", "banana", "cherry")



thistuple = ("apple", "banana", "cherry")
print(thistuple)



thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)



thistuple = ("apple", "banana", "cherry")
print(len(thistuple))




thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))




tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

"""Использование Asterisk*
Если число переменных меньше числа значений, можно добавить an к
имени переменной и Значения будут присваиваться переменной в виде списка:*
Остальные значения присвойте в виде списка с именем "red":"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)