with open('do-plecaka.txt', 'r') as f:
    dane = []
    # getting and cleaning data
    for line in f:
        dane.append([int(x) for x in line.split()])
    
# printing
for x in dane:
    print(x)