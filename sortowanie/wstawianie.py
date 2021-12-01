from losowe_liczby import losuj

tab = losuj(20)
print(tab)


for i in range(1, len(tab)):
    tymczasowe_miejsce = i

    for x in range(i, -1, -1): # szukamy miejsca do którego pasuje nowa zmienna
        if tab[i] < tab[x]:
            tymczasowe_miejsce = x
    tmp_var = tab[i]

    for l in range(tymczasowe_miejsce, i+1):  # wrzucamy zmienną do posortowanego zbioru
        tmp_var2 = tab[l]
        tab[l] = tmp_var
        tmp_var = tmp_var2

print(tab)