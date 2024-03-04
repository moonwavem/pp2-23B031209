class shape():
    def __init__ (self, length, width):
        self.length = length
        self.width = width
class rectangle(shape):
    def area(self):
        return (self.length * self.width)
        
a = rectangle(int(input(" 1:")), int(input(" 2:")))
print(rectangle.area(a))
