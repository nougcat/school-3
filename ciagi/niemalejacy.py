import sys
sys.path.insert(0, '../sortowanie/')
from losowe_liczby import losuj


def dlugosc_ciagu_ros(ciag):
    max_ciag = 1
    aktualny_ciag = 1
    for x in range(len(ciag)-1):
        if ciag[x] <= ciag[x+1]:
            print(ciag[x], ciag[x-1])
            aktualny_ciag += 1
            if max_ciag < aktualny_ciag:
                max_ciag = aktualny_ciag
        else:
            aktualny_ciag = 1
    return max_ciag

dlg_ciagu = int(input('podaj dlugosc ciagu: '))
ciag = losuj(dlg_ciagu)

print(ciag)

odp = dlugosc_ciagu_ros(ciag)
print(odp)