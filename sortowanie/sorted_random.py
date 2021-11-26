from random import randint, seed


def losuj(a):
    seed()
    liczby_losowe = []
    for x in range(a):
        liczby_losowe.append(randint(0, 99))
    for x in range(1, a):
        liczby_losowe[x] += liczby_losowe[x-1]
    return liczby_losowe

if __name__ == '__main__':
    tablica = losuj(10)
    print(tablica)