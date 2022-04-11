from random import randint

def ruch(pole, koordynaty):
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
        koordynaty[0] += 1
        return a
    else:
        koordynaty[1] += 1
        return b


wymiary=6
pole = []
for x in range(wymiary):
    pole += [[randint(1,9) for x in range(wymiary)]]
suma = 0

for x in pole:
    print(x)

koordynaty = [0,0]

while koordynaty != [wymiary-1,wymiary-1]:
    suma += ruch(pole, koordynaty)

print(pole[koordynaty[0]][koordynaty[1]])

print(suma)