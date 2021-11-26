from random import randint, seed 


def losuj(a):
    seed()
    liczby_losowe = []
    for x in range(a):
        liczby_losowe.append(randint(0, 99)) 
    return liczby_losowe

if __name__ == '__main__':
    tablica = losuj(10)
    print(tablica)