def celcium(fahrenheit):
    temp = (5 / 9) * (fahrenheit - 32)
    return temp
a = int(input())
print(" {} degrees".format(celcium(a)))