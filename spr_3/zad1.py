
def suma(n):
    return 0 if n<1 else n + suma(n-1)

print(suma(3))