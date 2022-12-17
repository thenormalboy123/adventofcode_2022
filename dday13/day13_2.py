###################################################################################
#  
#
#
###################################################################################

from ast import literal_eval
from itertools import zip_longest

def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0
    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)

def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    sorted_values = []
    for index, line in enumerate(Lines):
        if index%3 == 0 or index%3 == 1:
            value = literal_eval(line.strip())
            sorted_values.insert(0,value)
        else: #empty line   
            continue
    sorted_values.insert(0,[[2]]) # add dividers into sorted_values
    sorted_values.insert(0,[[6]]) # add dividers into sorted_values
    for i in range(1,len(sorted_values)): #insertion sort
        current_value = sorted_values[i]
        currentPos = i 
        while(currentPos > 0 and compare(sorted_values[currentPos - 1] , current_value) == 1):
            sorted_values[currentPos] = sorted_values[currentPos - 1]
            currentPos -= 1 
        sorted_values[currentPos] = current_value
    j = sorted_values.index([[2]]) #find index of [[2]] divider
    k = sorted_values.index([[6]]) #find index of [[6]] divider

    print((j+1)*(k+1)) # +1 since 1st entry has index 1 

main()