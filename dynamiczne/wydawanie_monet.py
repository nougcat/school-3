def wydaj_reszte(kwota, start):
    kwota_startowa = kwota
    reszta = [0 for x in (nominaly-start)]
    for i, x in enumerate(nominaly, start):
        if kwota % x != kwota:
            if kwota_startowa == kwota:
                reszta[i] = int(kwota/x)
            kwota = kwota % x
    return reszta

def max_kwota(kwota):
    for i, x in enumerate(nominaly):
        if kwota >= x:
            return i

nominaly = [500,200,100,50,20,10,5,2,1, 0.5 , 0.2, 0.1, 0.05, 0.02, 0.01]

if __name__=='__main__':
    kwota = float(input('podaj kwote: '))

    start = max_kwota(kwota)

    for x in enumerate(nominaly, start):
        print(wydaj_reszte(kwota, start))