
def bin(n):
    if n==1:
        print(n%2, end='')
    elif n>1:
        bin(n-1)
        print(n%2, end='')

print(bin(1))
print(bin(2))
print(bin(3))
print(bin(5))
print(bin(12))