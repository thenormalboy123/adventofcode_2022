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
    sum_of_indices = 0 
    left_values = []
    right_values = [] 
    for index, line in enumerate(Lines):
        if index%3 == 0:
            left_values = literal_eval(line.strip())
        elif index%3 == 1:
            right_values = literal_eval(line.strip())
            if (compare(left_values, right_values) != 1):
                sum_of_indices += int((index-1)/3)+1 #calculating the pair number and adding it to the sum 
        else: #empty line 
            continue

    print(sum_of_indices)


main()