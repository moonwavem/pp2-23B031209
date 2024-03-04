

#1
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#2
mytuple = ("banana","apple","cherry")


for x in mytuple:
    print(x)

#3 

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)

for t in myiter:
    print(t) 

class Car:
   def __init__(self,brand,model):
    self.brand = brand
    self.model = model

   def move(self):
    print("Drive!")

class Boat:
   def __init__(self,brand,model):
    self.brand = brand
    self.model = model

    def move(self):
      print("Sali!")
    
class Plane:
   def __init__(self,brand,model):
    self.brand = brand
    self.model = model

    def move(self):
      print("FLY!")

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing","747")

for x in (car1, boat1, plane1):
  x.move()


def myfunc():
    x = 300
    print(x)

myfunc()

