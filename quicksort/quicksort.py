def quicksort(tab):
    if len(tab) == 1:
        print(tab[0])
    
    else:
        mniejsze_var, wieksze_var = [], []
        wartownik = tab[0]
        for wartosc in tab:
            if wartosc < wartownik:
                mniejsze_var.append(wartosc)
            else:
                wieksze_var.append(wartosc)

        return quicksort(mniejsze_var) + print(wartownik) + quicksort(wieksze_var)


tab = [5, 14, 6, 7, 3, 2, 17, 33]
quicksort(tab)