from losowe_liczby import losuj

tab = losuj(20)

print(tab)

for x in range(len(tab)):
    min_num = tab[x]
    for i in range(x, len(tab)):
        if min_num > tab[i]:
            min_num = tab[i]
            min_loc = i
    if min_num != tab[x]:
        tab[min_loc] = tab[x] 
        tab[x] = min_num

print(tab)