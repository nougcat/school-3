def sortowanie(tekst: list) -> str:
    for x in range(len(tekst)-1):
        # jeśli litera jest większa to zamień
        if tekst[x] > tekst[x+1]:
            tekst[x], tekst[x+1] = tekst[x+1], tekst[x]
    odp = ''

    # zmieniamy listę na stringa
    for i in range(len(tekst)):
       odp += tekst[i] 
    return odp
if __name__=='__main__':
    # wczytujemy dane
    tekst = input('podaj tekst: ')
    sprawdz = input('podaj tekst: ')

    # sortujemy
    odp = sortowanie(list(tekst))
    odp2 = sortowanie(list(sprawdz))

    # sprawdzamy odpowiedzi
    if odp == odp2:
        print('anagramy')
    else:
        print('nie')