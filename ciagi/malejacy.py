def dlugosc_ciagu_ros(ciag):
    max_ciag = 1
    aktualny_ciag = 1
    for x in range(len(ciag)-1):
        if ciag[x] > ciag[x+1]:
            aktualny_ciag += 1
            if max_ciag < aktualny_ciag:
                max_ciag = aktualny_ciag
                indeks = x
        else:
            aktualny_ciag = 1
    return max_ciag, indeks+1

def losuj_dziennik(nr_dz):
    from random import randint, seed 
    seed()
    liczby_losowe = []
    a = 10 + nr_dz
    # losu losu
    for x in range(a):
        liczby_losowe.append(randint(-(nr_dz*2 - 20), (nr_dz*2 + 10)))

    return liczby_losowe
    

if __name__=='__main__':
    dlg_ciagu = int(input('podaj nr w dzienniku: '))
    patryk = losuj_dziennik(dlg_ciagu)

    print(patryk)

    odp, indeks = dlugosc_ciagu_ros(patryk)
    print(f'najdłuższy ciąg - {odp}')
    print(patryk[indeks-odp+1:indeks+1])