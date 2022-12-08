file1 = open('input.txt', 'r')
Lines = file1.readlines()
num_rows = len(Lines)
num_col = len(Lines[0].strip())
tree_map =  [[0 for x in range(num_col)] for y in range(num_rows)] 
tree_vision = [[0 for x in range(num_col)] for y in range(num_rows)] 
current_line = 0 
file1.seek(0)



for line in Lines:
    line_edited = line.strip()
    for index, i in enumerate(line_edited):
        tree_map[current_line][index] = int(i)
    current_line += 1 
    
for row in range(num_rows):
    for col in range(num_col):
        score_left = 0
        score_right = 0 
        score_up = 0
        score_down = 0  
        
# look left 
        for spaces in range(col):
            if tree_map[row][col] > tree_map[row][col-1-spaces]:
                score_left += 1
            else: 
                score_left += 1
                break
#look right 
        for spaces in range(num_col - col - 1):
            if tree_map[row][col] > tree_map[row][col + spaces + 1]:
                score_right += 1
            else: 
                score_right += 1
                break
#look up
        for spaces in range(row):
            if tree_map[row][col] > tree_map[row-1-spaces][col]:
                score_up += 1
            else: 
                score_up += 1
                break
#look down 
        for spaces in range(num_rows - row - 1):
            if tree_map[row][col] > tree_map[row+ spaces + 1][col]:
                score_down += 1
            else: 
                score_down += 1
                break
        tree_vision[row][col] = score_down * score_left * score_up * score_right

best_view = 0  
for i in range(num_rows):
    for j in range(num_col):
        if tree_vision[i][j] > best_view:
            best_view = tree_vision[i][j]

print(best_view)
