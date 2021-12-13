
slowo = input("podaj slowo: ")
print(slowo)
slowo = list(slowo)
for x in range(len(slowo)-1):                 # tworzymy pętle która będzie działała o jeden raza mniej niż jest długośc tablicy
    for j in range(len(slowo)-1):             # bierzemy kolejne elementy tablicy
        if slowo[j] < slowo[j+1]:             # jeśli dany element jest większy od następnego to zamień je
            slowo[j], slowo[j+1] = slowo[j+1], slowo[j]
    
for x in range(len(slowo)):
    print(slowo[x], end='')