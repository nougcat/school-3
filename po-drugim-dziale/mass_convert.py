suma = 0
# otwieramy plik
max = [0, 0]
min = [0, 999]

def min_and_max(dec_val_of_line, system):
    if dec_val_of_line > max[1]:
        max[0], max[1] = system, dec_val_of_line
    elif dec_val_of_line < min[1]:
        min[0], min[1] = system, dec_val_of_line

def to_dec(system, liczba):
    results = 0
    y = 0
    while y < len(liczba):
        dec_val = int(liczba) * (system ** (len(liczba)) - y - 1)
        results += dec_val
        y += 1
    print(results)
    return results
    

with open('wuz2-zad1-liczby.txt', 'r') as f:
    for x in f:
        linia = x.split()
        print(linia)
        # zapisujemy w jakim systemie jest liczba
        system = int(linia[0])
        liczba = linia[1]

        dec_val_of_line = to_dec(system, liczba) 
        suma += dec_val_of_line

        min_and_max(dec_val_of_line, system)
    
print(f'suma - {suma}')
print(min)
print(max)