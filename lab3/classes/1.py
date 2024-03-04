
class string:
    def __init__ (self, string):
        self.string = string

    def getString(self):
        print(self.string.upper())

    def printString(self):
        print(self.string.upper())


s = string(input())
s.getString()
s.printString()