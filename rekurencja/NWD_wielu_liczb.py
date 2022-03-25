def NWD(a, b):
    if a < b:
        a, b = b, a


    while a%b != 0:
        a, b = b, a%b
    return b

a = input('podaj liczby: ')

liczby = a.split()

liczby = [int(x) for x in liczby]

odp = NWD(liczby[0], liczby[1])

for x in range(2, len(liczby)):
    odp = NWD(odp, liczby[x])

print(odp)