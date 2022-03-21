from unittest import result


#ilosc_kand = int(input())

moce_kandt = input()

odp = [int(x) for x in moce_kandt.split()]

odp.sort(reverse=True)

for x in range(10):
    print(odp[x], end=' ')