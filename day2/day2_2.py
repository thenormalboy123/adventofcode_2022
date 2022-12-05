import sys 

if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    sum = 0

    for line in Lines: 
        if line[0] == 'A':   # OPPONENT CHOOSES ROCK 
            if line[2] == 'X':
                sum += 3
            elif line[2] == 'Y':
                sum += 4
            else: # line[2] == 'Z'
                sum += 8
        elif line[0] == 'B':  # OPPONENT CHOOSES PAPER
            if line[2] == 'X':
                sum += 1
            elif line[2] == 'Y':
                sum += 5
            else: # line[2] == 'Z'
                sum += 9
        else: #line[0] == 'C'  OPPONENT CHOOSES SCISSORS
            if line[2] == 'X':
                sum += 2
            elif line[2] == 'Y':
                sum += 6
            else: # line[2] == 'Z'
                sum += 7
    print(sum)


########################################################################################################################
# A = Rock --> +1
# B = Paper --> +2
# C = Scissors --> +3 
# X = LOSE --> +0
# Y = DRAW --> +3
# Z = WIN  --> +6
# Win is 6, draw is 3, lose = 0 
########################################################################################################################