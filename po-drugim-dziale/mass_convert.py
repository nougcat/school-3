import sys
suma = 0
# otwieramy plik
with open('wuz2-zad1-liczby.txt', 'r') as f:
    for x in f:
        linia = x.split()
        print(linia)
        # zapisujemy w jakim systemie jest liczba
        system = int(linia[0])
        liczba = linia[1]
        y = len(liczba)-1
        while y >= 0:
            print(f'{int(liczba[y])} - int(liczba[y])')
            print(system ^ (len(liczba)-2 - y))
            suma += int(liczba[y]) * (system ^ (len(liczba)-1 - y))

            print(suma)
            y -= 1
        sys.exit()
