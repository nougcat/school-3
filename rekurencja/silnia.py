def silnia(x):
    i = 1
    for i in range(1, x):
        x = x*i
        print(i)
    return x

var = silnia(int(input('dawaj liczbe ')))
print(var)