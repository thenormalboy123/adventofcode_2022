import sys 

if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    sum = 0

    for line in Lines: 
        if line[0] == 'A':   # OPPONENT CHOOSES ROCK 
            if line[2] == 'X':
                sum += 4
            elif line[2] == 'Y':
                sum += 8
            else: # line[2] == 'Z'
                sum += 3
        elif line[0] == 'B':  # OPPONENT CHOOSES PAPER
            if line[2] == 'X':
                sum += 1
            elif line[2] == 'Y':
                sum += 5
            else: # line[2] == 'Z'
                sum += 9
        else: #line[0] == 'C'  OPPONENT CHOOSES SCISSORS
            if line[2] == 'X':
                sum += 7
            elif line[2] == 'Y':
                sum += 2
            else: # line[2] == 'Z'
                sum += 6
    print(sum)


########################################################################################################################
# A / X = Rock --> X = 1
# B / Y = Paper --> Y = 2
# C / Z = Scissors --> Z = 3 
# Win is 6, draw is 3, lose = 0 
########################################################################################################################