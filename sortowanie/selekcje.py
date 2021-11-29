from losowe_liczby import losuj

tab = losuj(20)

print(tab)

for x in range(len(tab)):
    min_num = tab[x] # najmniejszą wartością jest początkowa wartość
    for i in range(x, len(tab)):        # pętla ta porównuje kolejne wartości w tablicy z tą początkową
        if min_num > tab[i]:
            min_num = tab[i]            # jak będzie mniejsza to mamy nowe $min_num
            min_loc = i
    if min_num != tab[x]:               # jeśli najmniejsza liczba nie jest liczbą początkową to zamiana
        tab[min_loc] = tab[x] 
        tab[x] = min_num

print(tab)