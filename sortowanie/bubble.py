from losowe_liczby import losuj

tablica = losuj(20)
print(tablica)

for x in range(len(tablica)-1):                 # tworzymy pętle która będzie działała o jeden raza mniej niż jest długośc tablicy
    for j in range(len(tablica)-1):             # bierzemy kolejne elementy tablicy
        if tablica[j] > tablica[j+1]:           # jeśli dany element jest większy od następnego to zamień je
            tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
    
for x in tablica:
    print(x, end=' ')