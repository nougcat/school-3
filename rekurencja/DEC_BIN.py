# zamiana jednostek - rekurencja

def CyfryRek(n):
    if n<2: print(int(n))
    else:
        CyfryRek(n/2)
        print(int(n%2))

n = 532
CyfryRek(n)