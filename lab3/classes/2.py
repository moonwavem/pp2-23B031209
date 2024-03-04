class shape:
    def __init__(self):
        self.s = 0
    def area(self):
        print(self.s)

class square(shape):
    def __init__(self,length):
        shape.__init__(self)
        self.length = length
        self.s = self.length**2

x1 = shape()
x2 = square(4)
x1.area()
x2.area()