# liczymy ilość wystąpień w słowie
def sortowanie(tekst:str) -> list:
    tab = [0 for x in range(26)]
    for x in range(len(tekst)):
        tab[ord(tekst[x].upper()) - ord('A')] += 1
    return tab

if __name__=="__main__":
    # wczytujemy teksty
    tekst1 = input('podaj 1 tekst: ')
    tekst2 = input('podaj 2 tekst: ')
    tekst3 = input('podaj 3 tekst: ')

    # czy taka sama długość
    if len(tekst1) != len(tekst2) or len(tekst2) != len(tekst3):
        print('nie pasują')
    else:
        odp = sortowanie(tekst1)
        odp2 = sortowanie(tekst2)
        odp3 = sortowanie(tekst3)

        # czy odpowiedzi się zgadzają
        if odp == odp2 == odp3:
            print('tak')
        else:
            print('nie')