from random import random


def losuj(a):
    import random
    random.seed()
    liczby_losowe = []
    for x in range(a):
        liczby_losowe.append(random.randint(0, 99)) 
    return liczby_losowe

if __name__ == '__main__':
    a = 10
    x = losuj(a)
    print(x)