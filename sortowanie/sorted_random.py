from random import randint, seed


def losuj(a):
    # sadzimy
    seed()
    liczby_losowe = []

    # losu losu
    for x in range(a):
        liczby_losowe.append(randint(0, 99))

    # dodajemy poprzednią liczbę do wylosowanej - tak aby to wszystko bylo posortowane
    for x in range(1, a):
        liczby_losowe[x] += liczby_losowe[x-1]

    return liczby_losowe

if __name__ == '__main__':
    tablica = losuj(10)
    print(tablica)