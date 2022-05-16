ilosc_x = 0
ilosc_txt = 0
min_slowo = 'SOOJVVLCWRGGZHFJCFSQKJ'

with open('sygnaly.txt','r') as f:
    for line in f:
        print(line)
        for x in range(len(line)):
            # ile jest "x" w linijce
            if line[x] == "X":
                ilosc_x += 1
            # ile jest "txt" w linijce
            if  x > 0 and x < len(line) and line[x-1] == "T" and line[x] == "X" and line[x+1] == "T":
                ilosc_txt += 1
        # najkrotsze slowo w pliku
        if len(line) < len(min_slowo):
            min_slowo = line

print(f'ilosc txt = {ilosc_txt}')
print(f'ilosc x = {ilosc_x}')
print(f'najkrotsze slowo = {min_slowo}')