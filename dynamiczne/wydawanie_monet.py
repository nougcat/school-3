def wydaj_reszte(kwota, start):
    # tworzymy pustą tablicę
    reszta = [0 for x in (nominaly)]

    for i in range(start, len(nominaly)):
        if kwota % nominaly[i] != kwota:
            reszta[i] = int(kwota/nominaly[i])
            kwota = kwota % nominaly[i]
    
    return reszta

def max_kwota(kwota):
    # usunięcie największych nominalów jeśli nie jest potrzebne
    for i, x in enumerate(nominaly):
        if kwota >= x:
            return i

def min_nominalow(reszty):
    # najmiejsza ilość nominałów do wydania reszty
    min_ilosc_nominalow = not None
    for x in reszty:
        aktualna_ilosc_nominalow = 0
        for i in x:
            aktualna_ilosc_nominalow += i
        if min_ilosc_nominalow > aktualna_ilosc_nominalow: min_ilosc_nominalow = aktualna_ilosc_nominalow
        print(aktualna_ilosc_nominalow)
        print(min_ilosc_nominalow)
    return min_ilosc_nominalow

nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5 , 0.2, 0.1, 0.05, 0.02, 0.01]

if __name__=='__main__':
    kwota = float(input('podaj kwote: '))

    start = max_kwota(kwota)

    reszty = []
    start -= 1
    for x in range(start, len(nominaly)-1):
        start += 1
        reszty.append(wydaj_reszte(kwota, start))

    print(min_nominalow(reszty))