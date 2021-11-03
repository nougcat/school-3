k = input('podaj k:')
l = input('podaj l:')

anagram = True

for x in range(len(k)):
    if k[x] != l[-(x+1)]:
        anagram = False

if anagram:
    print("TAK")
else:
    print("NIE")
