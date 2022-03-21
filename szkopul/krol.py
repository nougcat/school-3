input = input('')
dane = input.split()
ilosc_scian = 0
dane[1] = int(dane[1])

# sprawdzamy czy król jest koło ściany
if dane[0] in {'a', 'h'}:
    ilosc_scian += 1

if dane[1] in {1, 8}:
    ilosc_scian +=1


# odp zależna od ilości ścian
if ilosc_scian == 2:
    print(3)
elif ilosc_scian == 1:
    print(5)
else:
    print(8)