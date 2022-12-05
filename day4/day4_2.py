import re

if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    count = 0

    for line in Lines: 
        line_tochange = re.split(r'[-,]', line.strip())
        if ( (int(line_tochange[0]) >= int(line_tochange[2])) and (int(line_tochange[0]) <= int(line_tochange[3])) ): 
            count+=1
        elif ( (int(line_tochange[1]) >= int(line_tochange[2])) and (int(line_tochange[1]) <= int(line_tochange[3])) ): 
            count+=1
        elif ( (int(line_tochange[2]) >= int(line_tochange[0])) and (int(line_tochange[2]) <= int(line_tochange[1])) ): 
            count+=1
        elif ( (int(line_tochange[3]) <= int(line_tochange[0])) and (int(line_tochange[3]) >= int(line_tochange[1])) ): 
            count+=1
    print(count)

