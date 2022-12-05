import sys 

if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    total_priority = 0
    lines = 0 

    for line in Lines:
        lines += 1
        foundflag=False
        compartment_size = (len(line)-1) / 2
        for i in range(int(compartment_size)):
            for j in range(int(compartment_size)):
                if line[i] == line[j+int(compartment_size)]:
                    if line[i].islower():
                        total_priority += ( ord(line[i]) - 96 )
                    else:
                        total_priority += ( ord(line[i]) - 38 )                    
                    foundflag = True
                    break
            if foundflag: break


    print(total_priority)