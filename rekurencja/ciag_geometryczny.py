def rek(a):
    if a == 0: return 1
    else:
        x = rek(a-1) * 2
        return x

x = rek(5)

print(x)