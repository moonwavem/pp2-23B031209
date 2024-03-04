def ounces(gramm):
    ounce = 28.3495231 * gramm
    return ounce
a = int(input())
print("You need {} ounces".format(ounces(a)))