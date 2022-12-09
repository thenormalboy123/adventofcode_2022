#########################################################################
# Note: you may need to update your python version to v3.10 or above for 
# the switch statement to work 
#########################################################################



#adjacency checker returns 0 if it's aligned, 1 if only 1D adjustment is needed, 2 if 2D adjustment is needed 
def adjacency_checker(head_x, head_y, tail_x, tail_y):
    if head_x == tail_x:
        if abs(tail_y-head_y) <=1: 
            return 0 
        else:
            return 1 
    elif head_y == tail_y:
        if abs(tail_x-head_x) <=1: 
            return 0 
        else:
            return 1
    elif abs(tail_y-head_y) ==1 and abs(tail_x-head_x) ==1: #diagonally touching counts as adjacent
        return 0 
    else: 
        return 2

def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    #set up the map for tail trail, assume 450*450 
    tail_trail = [[0 for x in range(450)] for y in range(450)]
    #assume the starting position at 200,10, values here are obtained through trial and error 
    head_x, head_y = 200,10
    tail_x, tail_y = 200,10

    for index, line in enumerate(Lines): 
        instructions = line.strip().split(' ')
        tail_trail[200][10] = 1 # mark starting position as part of trail

        match instructions[0]:
            case 'R':
                for _ in range(int(instructions[1])):                 
                    head_x +=1 
                    if adjacency_checker(head_x, head_y, tail_x, tail_y) == 1:
                        tail_x += 1 
                    elif adjacency_checker(head_x, head_y, tail_x, tail_y) == 2:
                        tail_x += 1
                        tail_y = head_y # move diagonally 
                    tail_trail[tail_x][tail_y] = 1 
            case 'L':
                for _ in range(int(instructions[1])):                     
                    head_x -=1 
                    if adjacency_checker(head_x, head_y, tail_x, tail_y) == 1:
                        tail_x -= 1 
                    elif adjacency_checker(head_x, head_y, tail_x, tail_y) == 2:
                        tail_x -= 1
                        tail_y = head_y # move diagonally 
                    tail_trail[tail_x][tail_y] = 1
            case 'U':
                for _ in range(int(instructions[1])):                     
                    head_y -=1 
                    if adjacency_checker(head_x, head_y, tail_x, tail_y) == 1:
                        tail_y -= 1 
                    elif adjacency_checker(head_x, head_y, tail_x, tail_y) == 2:
                        tail_y -= 1
                        tail_x = head_x # move diagonally 
                    tail_trail[tail_x][tail_y] = 1
            case'D': 
                for _ in range(int(instructions[1])):                    
                    head_y +=1 
                    if adjacency_checker(head_x, head_y, tail_x, tail_y) == 1:
                        tail_y += 1 
                    elif adjacency_checker(head_x, head_y, tail_x, tail_y) == 2:
                        tail_y += 1
                        tail_x = head_x # move diagonally 
                    tail_trail[tail_x][tail_y] = 1
            case _:
                print("Error in using python match instructions")

        print(f"At instructions {index+1}, Current head position: head_x = {head_x}, head_y = {head_y}")
    answer = 0 
    for i in range(450):
        for j in range(450):
            if tail_trail[i][j] == 1:
                answer +=1

    print(answer)


main()