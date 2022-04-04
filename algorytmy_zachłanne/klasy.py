def add_to_array(line):
    line = line.split()
        
    line[1] = line[0] + line[1]/60



if __name__ == '__main__':
    from array import array

    with open('dane.txt','r') as f:
        for line in f:
            add_to_array(line)
    
    

        
