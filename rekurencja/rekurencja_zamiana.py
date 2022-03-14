# zamiana jednostek - rekurencja

from itertools import count

def CyfryRek(n):
    if n<10: print(int(n))
    else:
        CyfryRek(n/10)
        print(int(n%10))

n = 532
CyfryRek(n)