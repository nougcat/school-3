# zamiana jednostek - rekurencja

def CyfryRek(n):
    if n<2: print(int(n),end='')
    else:
        CyfryRek(n/2)
        print(int(n%2),end='')

n = 532
CyfryRek(n)