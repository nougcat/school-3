# wypisujemy dzielniki liczby

i = int(input(''))

# if num is 1
if i == 1:
    print(1)
    exit()

# printing first divisor
print(1)

# printing all divisor (except first and last)
for x in range(2, i-1):
    if i%x == 0:
        print(x)

print(i)