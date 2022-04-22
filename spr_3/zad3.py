def ruch(pole, koordynaty, nieparzyste):
    nieparzyste = 0
    print(pole[koordynaty[0]][koordynaty[1]])

    if koordynaty[0] == wymiary-1:
        a = 0
    else:
        a = pole[koordynaty[0]+1][koordynaty[1]]
    if koordynaty[1] == wymiary-1:
        b = 0
    else:
        b = pole[koordynaty[0]][koordynaty[1]+1]
    
    if a >= b:
        if not a%2: nieparzyste += 1
        koordynaty[0] += 1
        return a, nieparzyste
    else:
        if not b%2: nieparzyste +=1
        koordynaty[1] += 1
        return b, nieparzyste


wymiary = 4
pole = []

with open('mswk.txt', 'r') as f:
    for x in f:
        linijka = x.split()
        linijka_arr = []
        for i in linijka:
            linijka_arr.append(int(i))
        pole.append(linijka_arr)

suma = int(pole[0][0])

nieparzyste = 0

if not int(pole[0][0])%2: nieparzyste = 1
else: nieparzyste = 0


for x in pole:
    print(x)

koordynaty = [0,0]

while koordynaty != [wymiary-1,wymiary-1]:
    x = ruch(pole, koordynaty, nieparzyste)
    suma += x[0]
    nieparzyste += x[1]

print(pole[koordynaty[0]][koordynaty[1]])

print(f'suma: {suma}, nieparzystych: {nieparzyste-1}')