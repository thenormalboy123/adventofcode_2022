import sys 

if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    total_priority = 0
    lines = 0 
    bagsof3 = ["string1","string2"]

    for line in Lines:
        if (lines<2):
            bagsof3[lines] = line
            lines+=1
        else: 
            for i in range(len(line)):
                if (line[i] in bagsof3[0] and line[i] in bagsof3[1]):
                    if line[i].islower():
                        total_priority += ( ord(line[i]) - 96 )
                    else:
                        total_priority += ( ord(line[i]) - 38 )
                    break
            lines = 0

    print(total_priority)