from losowe_liczby import losuj

tab = losuj(20)
print(tab)
for i in range(len(tab)-1):
    for x in range(i, 0 , -1):
        if tab[i] < tab[x]:
            min_loc = x
    
    for l in range(min_loc, i):
        tab[l], tab[l+1] = tab[l+1], tab[l]