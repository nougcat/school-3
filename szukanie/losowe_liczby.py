from random import random


def losuj(a):
    import random
    random.seed()
    liczby_losowe = []
    for x in range(a):
        liczby_losowe.append(random.randint(0, 100))
    for x in range(1, a):
        liczby_losowe[x] += liczby_losowe[x-1]
    return liczby_losowe

if '__main__' == __name__:
    a = 10
    x = losuj(a)
    print(x)