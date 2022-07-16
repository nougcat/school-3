def bin(a):
    if a == 1:
        return 1
    else:
        return ( str(bin(int(a/2))) + str(a%2) )

# a = input('podaj liczbe: ')
for x in [1,2,3,4,5,6,7]:
    print(bin(x))