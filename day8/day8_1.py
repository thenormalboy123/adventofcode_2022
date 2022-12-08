
file1 = open('input.txt', 'r')
Lines = file1.readlines()
num_rows = len(Lines)
num_col = len(Lines[0].strip())
tree_map =  [[0 for x in range(num_col)] for y in range(num_rows)] 
tree_vision = [[0 for x in range(num_col)] for y in range(num_rows)] 
current_line = 0
visible_tree = 0 #number of visible trees 
file1.seek(0)

# read file, another way will be used in day8_2.py
for line in Lines:
    line_edited = line.strip()
    tree_map[current_line] = list(line_edited)
    current_line += 1 
    
#view from left 

for row in range(num_rows):
    for col in range(num_col):
        if col == 0: #edges are always visible
            tallest_tree = int(tree_map[row][0])
            tree_vision[row][0] += 1
        elif int(tree_map[row][col]) > tallest_tree: #if tree is taller than all trees before it 
                tallest_tree = int(tree_map[row][col]) # this tree is the tallest tree up to that column
                tree_vision[row][col] += 1 #set it as visible 
        else: 
            pass
        tree_vision[row][col] += 1

#view from right 

for row in range(num_rows):
    for col in range(num_col-1, 0, -1):
        if col == num_col - 1 : #edges are always visible
            tallest_tree = int(tree_map[row][num_col - 1])
            tree_vision[row][num_col-1] += 1
        else: 
            if int(tree_map[row][col]) > tallest_tree: #if tree is taller than all trees before it 
                tallest_tree = int(tree_map[row][col]) # this tree is the tallest tree up to that column
                tree_vision[row][col] += 1 #set it as visible 

#view from top 

for col in range(num_col):
    for row in range(num_rows):
        if row == 0:
            tallest_tree = int(tree_map[0][col])
            tree_vision[0][col] += 1
        else: 
            if int(tree_map[row][col]) > tallest_tree: #if tree is taller than all trees before it 
                tallest_tree = int(tree_map[row][col]) # this tree is the tallest tree up to that column
                tree_vision[row][col] += 1 #set it as visible 

#view from bottom

for col in range(num_col):
    for row in range(num_rows-1, 0, -1):
        if row == num_rows-1:
            tallest_tree = int(tree_map[num_rows-1][col])
            tree_vision[num_rows-1][col] += 1
        else: 
            if int(tree_map[row][col]) > tallest_tree: #if tree is taller than all trees before it 
                tallest_tree = int(tree_map[row][col]) # this tree is the tallest tree up to that column
                tree_vision[row][col] += 1 #set it as visible 


#count how many trees are visible 

for i in range(num_rows):
    for j in range(num_col):
        if tree_vision[i][j] > 1:
            visible_tree += 1 

print(visible_tree)
file1.close()
