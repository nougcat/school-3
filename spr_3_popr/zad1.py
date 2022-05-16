def suma(n):
    return -1 if n==1 else - (suma(n-1) * n) - 3

print(suma(1))
print(suma(2))
print(suma(3))
print(suma(4))
print(suma(5))