from losowe_liczby import losuj

tab = losuj(20)

print(tab)

for x in range(len(tab)-1):                 # tworzymy pętle która będzie działała o jeden raza mniej niż jest długośc tablicy
    for j in range(len(tab)-1):             # bierzemy kolejne elementy tablicy
        if int(str(tab[j])[-1]) > int(str(tab[j+1])[-1]):           # jeśli dany element jest większy od następnego to zamień je
            tab[j], tab[j+1] = tab[j+1], tab[j]
    

print(tab)