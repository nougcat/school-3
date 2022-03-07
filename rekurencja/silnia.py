def silnia(x):
    if x==1:
        return 1
    return silnia(x-1)*x

var = silnia(7)
print(var)