#2 
class shape():
    def __init__ (self, length):
        self.length = length
class square(shape):
    def area(self):
        return (self.length ** 2)
        
a = square(int(input("введите сторону:")))
print(square.area(a))
#1
class string:
    def __init__ (self, string):
        self.string = string

    def getString(self):
        print(self.string)

    def printString(self):
        print(self.string.upper())


s = string(input())
s.getString()
s.printString()

#3
class shape():
    def __init__ (self, length, width):
        self.length = length
        self.width = width
class rectangle(shape):
    def area(self):
        return (self.length * self.width)
        
a = rectangle(int(input("введите сторону 1:")), int(input("введите сторону 2:")))
print(rectangle.area(a))

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, z , z1):
        self.x = self.x + z
        self.y = self.y + z1
    def __str__(self):
        return f"({self.x};{self.y})"
    def dic(self, x , y):
        z = self.x - x
        z1 = self.y - y
        print((math.sqrt((z)**2 + (z1)**2)))
print("Coordinates of first point")
x1 = int(input())
y1 = int(input())
print("x =" , x1 , "y =" , y1)
print(" second point")
x2 = int(input())
y2 = int(input())
print("x = " , x2 , "y = " , y2)
p1 = Point(x1 , y1)
p2 = Point(x2,y2)
print("first and second:")
p1.dic(x2 , y2)
print("X at the first point")
movep1x = int(input())
print("Y at the first point")
movep1y = int(input())
print(" X at the second point")
movep2x = int(input())
print("Y at the second point")
movep2y = int(input())
p1.move(movep1x,movep1y)
p2.move(movep2x,movep2y)
print("First p")
print(p1)
print("Second p")
print(p2)

#5
class Account:
    def __init__(self, owner, balance = 0):
        self.o = owner
        self.b = balance
    def __str__(self):
        return ("Account owner: {} \nAccount balance: {}").format(self.o, self.b )
    def deposit(self, deposit):
        self.b = self.b + deposit
        print("+ {} \nYour current balance is {} tenge.".format(deposit,self.b))
    def withdraw(self, w):
            if w > self.b:
                print("Error, insufficient funds \nYour current balance is {}".format(self.b))
            else:
                self.b = self.b - w
                print("Withdrawal Accepted \nYour current balance is {}".format(self.b))
a = str(input("Give your account a name: \n"))
p = Account(a)
print(p)
ans = input("What would you like to do with your account?\nIf nothing, write \'No\'\n")
while ans != 'No':
    if ans == 'Deposit':
        q = int(input())
        p.deposit(q)
    elif ans == 'Withdraw':
        x = int(input())
        p.withdraw(x)
    ans = input("Do you want to continue operations?\nIf so, then write the operation or you can write \'No\'.\n")
        
print('Have a good day!')

#6
import math


def primes(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

a = list(map(int, input("Enter").split()))
res = list(filter(lambda x: (primes(x) == True), a))
print(res)