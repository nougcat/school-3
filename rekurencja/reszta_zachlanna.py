def dawaj_reszte(kwota):
    ini_kwota = kwota
    reszta = []
    for x in nominaly:
        if kwota % x != kwota:
            if ini_kwota == kwota:
                ile_razy = int(kwota/x)
            reszta += [x]
            kwota = kwota % x
    return reszta, ile_razy


if __name__=='__main__':
    nominaly = [500,200,100,50,20,10,5,2,1, 0.5 , 0.2, 0.1, 0.05, 0.02, 0.01]

    a = float(input('podaj kwote: '))

    reszta, ile_razy = dawaj_reszte(a)

    for x in reszta:
        if x == reszta[0]:
            if x >=1:
                print(f'{ile_razy} * {x}zł')
            else:
                print(f'{ile_razy} * {int(x * 100)}gr')

        elif x>=1:
            print(f'1 * {x}zł')
        else:
            print(f'1 * {int(x * 100)}gr')