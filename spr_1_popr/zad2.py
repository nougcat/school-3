x = int(input('podaj liczbe: '))
suma = 0
for i in range(len(str(x))):
    suma += int(str(x)[i])

print(suma)