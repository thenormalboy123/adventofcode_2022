###################################################################################
# Smallest x-value is 432, smallest y-value is 13 
# Largest x-value is 518, largest y-value is 156
# 
#
###################################################################################

sandmap = [['.' for x in range(530)] for y in range(160)]

def abyssChecker(x,y):
    for a in range(y-1,0,-1):
        if sandmap[a][x] != '.':
            return 0 
    return 1

def MapPrinter(): # does not contribute to solution, just for me to check my map 
    for i in range(160):
        print()
        for j in range(95): # for readability after printing 
            print(sandmap[i][j+430], end='')

def SandFlow():
    global sandmap 
    sand_count = 0
    try:
        while(1): #while abyss not reached
            sand_count += 1
            sand_x = 500 
            sand_y = 0 
            while (1): # while sand can still move
                if sandmap[sand_y+1][sand_x] == '.':
                    sand_y += 1 
                elif sandmap[sand_y+1][sand_x-1] == '.':
                    sand_y += 1
                    sand_x -= 1 
                elif sandmap[sand_y+1][sand_x+1] == '.':
                    sand_y += 1
                    sand_x += 1 
                else: 
                    sandmap[sand_y][sand_x] = '0'
                    break

    except IndexError:
        print(f"Overflow occured at {sand_x} {sand_y}")
        MapPrinter()
        print(sand_count-1) #last sand does not come to rest since it flows into abyss 

def main():
    global sandmap
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    for line in Lines: #iterate through all lines in entry.txt
        a = line.strip().split(' -> ')
        for index in range(1,len(a)): #iterate through all coordinates in a line
            if a[index].split(',')[0] == a[index-1].split(',')[0]: #if x-value is same 
                current_tile = int(a[index].split(',')[1]) 
                sandmap[current_tile][int(a[index].split(',')[0])] = '#'
                while current_tile != int(a[index-1].split(',')[1]): 
                    if current_tile < int(a[index-1].split(',')[1]):
                        current_tile += 1
                        sandmap[current_tile][int(a[index].split(',')[0])] = '#'
                    else:
                        current_tile -= 1
                        sandmap[current_tile][int(a[index].split(',')[0])] = '#'
            else: #y-value is same 
                current_tile = int(a[index].split(',')[0]) 
                sandmap[int(a[index].split(',')[1])][current_tile] = '#'
                while current_tile != int(a[index-1].split(',')[0]): 
                    if current_tile < int(a[index-1].split(',')[0]):
                        current_tile += 1
                        sandmap[int(a[index].split(',')[1])][current_tile] = '#'
                    else:
                        current_tile -= 1
                        sandmap[int(a[index].split(',')[1])][current_tile] = '#'
    SandFlow()



main()