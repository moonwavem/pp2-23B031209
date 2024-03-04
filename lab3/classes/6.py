def prime(n):
    if n < 2: return False 
    for i in range (2, int(n**(1/2)+1)):
        if n % i ==0:
            return False
    return True

l = [ -4, -3, -2, -1, 0, 1, 2, 3, 4, ]
nums = list(filter(lambda x:prime(x),l))
print (nums)