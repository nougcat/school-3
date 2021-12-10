# liczymy ilość wystąpień w słowie
def sortowanie(tekst:str) -> list:
    tab = [0 for x in range(26)]
    for x in range(len(tekst)):
        tab[ord(tekst[x].upper()) - ord('A')] += 1
    return tab

if __name__=="__main__":
    # wczytujemy teksty
    tekst = input('podaj 1 tekst: ')
    sprawdzam = input('podaj 2 tekst: ')

    # czy taka sama długość
    if len(tekst) != len(sprawdzam):
        print('nie pasują')
    else:
        odp = sortowanie(tekst)
        odp2 = sortowanie(sprawdzam)

        # czy odpowiedzi się zgadzają
        if odp == odp2:
            print('to jest anagram')
        else:
            print('to nie jest anagram')