#check palindrom
def d(num, test):
    rev = ''.join(list(reversed(test)))
    print('Test #{} is {} palindrom'.format(num, 'a' if rev == test else 'not a'))


a = input()

d(1, a)

