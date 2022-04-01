def dawaj_reszte(kwota):
    reszta = []
    for x in nominaly:
        if kwota % x != kwota:
            reszta += [x * int((kwota/x))]
            kwota = kwota % x
    return reszta

nominaly = [500,200,100,50,20,10,5,2,1, 0.5 , 0.2, 0.1, 0.05, 0.02, 0.01]

a = int(input('podaj kwote: '))

reszta = dawaj_reszte(a)

print(reszta)