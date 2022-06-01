def quicksort(tab):
    if len(tab) == 1:
        print(tab[0])
    
    else:
        mniejsze_var, wieksze_var = [], []
        wartownik = tab[0]
        print(tab)
        for x in range(1, len(tab)):
            if tab[x] < wartownik:
                mniejsze_var.append(tab[x])
            elif tab[x] > wartownik:
                wieksze_var.append(tab[x])
        return quicksort(mniejsze_var), print(wartownik), quicksort(wieksze_var)


tab = [5, 14, 6, 7, 3, 2, 17, 33]
quicksort(tab)