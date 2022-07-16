def rec(a):
    if a < 2:
        return 1
    else:
        return ( rec(a-1) + rec(a-2) )


# a = input('podaj liczbe: ')
for x in [0,1,2,3,4,5,6,7]:
    print(rec(x))