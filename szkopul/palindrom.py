def czy_pal(tekst):
    for x in range(len(tekst)):
        if tekst[x] != tekst[len(tekst)-1-x]:
            return False
    return True

def nowy_pal(tekst):
    odp = tekst
    for x in range(len(tekst)):
        odp += tekst[len(tekst)-1-x]
    
    return odp


tekst = input()

results = czy_pal(tekst)

if results:
    print('tak')
else:
    nowy_tekst = nowy_pal(tekst)
    print(nowy_tekst)


