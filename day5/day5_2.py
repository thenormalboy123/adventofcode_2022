import re

if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    stack_index = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    stack = [[],[],[],[],[],[],[],[],[]]
    line_number = 1
    final_output = ''
    for line in Lines:
        if (line_number < 9):
            current_stack = 0
            for index in stack_index:
                if (len(line) <= stack_index[current_stack]):
                    pass
                elif (line[stack_index[current_stack]] == ' '):
                    pass
                else:
                    stack[current_stack].insert(0, line[stack_index[current_stack]])
                current_stack+=1
        elif('move' in line):
            line_modified = line.strip()
            line_modified = line_modified.replace('move', 'to')
            line_modified = line_modified.replace('from', 'to')
            movement_instruction = line_modified.split('to') # move movement_instruction[1] from movement_instruction[2] to movement_instruction[3]

            
            for i in range(len(movement_instruction)-1): # convert str to int 
                movement_instruction[i+1] = int(movement_instruction[i+1].strip())
            
            if (len(stack[movement_instruction[2] - 1]) < movement_instruction[1]): # move all crates if instruction exceeds number of crates in stack 
                movement_instruction[1] = len(stack[movement_instruction[2] - 1])
            
            for moves in range(movement_instruction[1]):
                moved_item = stack[movement_instruction[2] - 1][len(stack[movement_instruction[2] - 1]) - movement_instruction[1] + moves] 
                stack[movement_instruction[3] - 1].append(moved_item)
                
            for moves in range(movement_instruction[1]): # remove moved items from previous stack 
                stack[movement_instruction[2] - 1].pop()

        else:
            continue
        line_number+=1
#print top item in stack 
    for col in stack: 
        final_output += col[len(col) - 1]
        
    print(final_output)
