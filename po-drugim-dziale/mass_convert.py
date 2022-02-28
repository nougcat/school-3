suma = 0
# otwieramy plik
max = [0,0]
min = [-1]

def min_and_max(dec_val_of_line, system):
    if min[0] == -1:
        min[0] = system
        min.append(dec_val_of_line)
    
    if dec_val_of_line > max[1]:
        max[0], max[1] = system, dec_val_of_line
    elif len(min) == 2 and dec_val_of_line < min[1]:
        min[0], min[1] = system, dec_val_of_line
    
    

with open('wuz2-zad1-liczby.txt', 'r') as f:
    for x in f:
        linia = x.split()
        print(linia)
        # zapisujemy w jakim systemie jest liczba
        system = int(linia[0])
        liczba = linia[1]
        y = 0
        while y < len(linia[1]):
            print(system ** (len(linia[1])-y))
            print(f'dupa {y}')
            print(liczba[y])
            
            dec_val_of_line = int(liczba[y]) * (system ** (len(linia[1]) - y - 1))
            suma += dec_val_of_line
            y += 1

            min_and_max(dec_val_of_line, system)
    
print(f'suma - {suma}')
print(min)
print(max)