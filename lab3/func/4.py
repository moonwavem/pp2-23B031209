def filter_prime(l):
    nwl = []
    for i in l:
        check = True  # Переместим это объявление в цикл for
        for j in range(2, int(pow(i, 1/2)) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            nwl.append(i)
    return nwl

arr = list(map(int, input().split()))

result = filter_prime(arr)
print(result)


    