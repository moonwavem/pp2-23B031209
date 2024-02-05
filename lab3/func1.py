#1
def ounces(gramm):
    ounce = 28.3495231 * gramm
    return ounce
a = int(input("Enter "))
print("You need {} ounces".format(ounces(a)))

#2
def celcium(fahrenheit):
    temp = (5 / 9) * (fahrenheit - 32)
    return temp
a = int(input("Enter "))
print(" {} degrees".format(celcium(a)))

#3
def animals(legs, heads):
    rabbit = (legs - (heads * 2))/2
    chicken = heads - rabbit
    print("rabbits ", int(rabbit))
    print("chickens ", int(chicken))
a = int(input(" legs: "))
b = int(input("heads: "))
animals(a, b)

#4
def primes(lisst):
    list2 = set()
    u = 0
    while u < len(lisst):
        if (lisst[u] == 2) or (lisst[u] == 3):
                list2.add(lisst[u])
        for i in range(2, (int(lisst[u] / 2) + 1)):
            if lisst[u] % i != 0:
                list2.add(lisst[u])
                continue
            else:
                break
        u += 1
    print(list2)

q =  list(map(int, input('Enter').split()))
primes(q)
#5
def spy(lisst):
    srav = list()
    for i in range(len(lisst)):
        if lisst[i] == 7:
            srav.append(i)
            break
        elif lisst[i] == 0:
            srav.append(i)
    srav2 = srav.copy()
    srav2.sort()
    if srav2 == srav and len(srav) >= 3:
        print(bool(1))
    else:
        print(bool(""))

a = list(map(int, input('Enter').split()))
spy(a)
#13
import random

print("Hello! What is your name?")
a = str(input())
qw = int(random.randint(1, 20))
q = 1
print('Well, %s, I am thinking of a number between 1 and 20.' % a)
print("Take a guess.")
num = int(input())
while num != qw:
    if (num > qw):
        print("Your guess is too high.")
        print("Take a guess.")
        q += 1
    elif num < qw:
        print("Your guess is too low.")
        print("Take a guess.")
        q += 1
    num = int(input())

print('Good job, %s! You guessed my number in %s guesses!' %(a, q))

#7
def perm(stroka, bykva = ''):
    if len(stroka) == 0:
        print(bykva)
    for i in range(len(stroka)):
        word = bykva + stroka[i]
        novyistroka = stroka[0:i] + stroka[i + 1:]
        perm(novyistroka, word)
a = str(input())
print(perm(a))
#6
def rev(lisst):
    sentlist = lisst.split()
    reverlist = reversed(sentlist)
    print(" ".join(reverlist))

a = str(input("Enter "))
rev(a)
#10
def has_33(lisst):
    q = 0
    for i in range(len(lisst) - 1):
        if (lisst[i] == 3) and (lisst[i+1] == 3):
            q = 1
            break
    if q == 1:
        print(bool(1))
    else:
        print(bool(""))
a = list(map(int, input('Enter').split()))
has_33(a)

#9
def arrea(rr):
    areasp = 4 * 3.14 * rr * rr
    print("Full area of sphere = ", areasp)

print('Enter ')
r = int(input())
arrea(r)

#8
def unique_list(numbers):
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
    return unique

a = list(map(int, input('Enter s').split()))
print("Unique list:", unique_list(a))

#11
def pali(word):
    if word == word[::-1]:
        return True
    else:
        return False

a = str(input())
print(pali(a))
#12
def histogram(lisst):
    i = 0
    while i < len(lisst):
        for x in lisst:
            print('*' * lisst[i])
            break
        i += 1

a = list(map(int, input('Enter').split()))
print(histogram(a))