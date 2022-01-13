# sprawdzamy czy liczba jest pierwsza

i = int(input(''))

if i == 1:
    print('Nie')
    exit()

for x in range(2, i-1):
    if i%x == 0:
        print('Nie')
        exit()

print('Tak')