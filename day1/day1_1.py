if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    highest_calorie = 0

    current_calorie_count = 0
    top3calories = []
    arrayentry = 0

    for line in Lines: 
        if (len(line.strip()) == 0): #if empty line aka elf is not carrying anymore calories
            if current_calorie_count > highest_calorie:
                highest_calorie = current_calorie_count
            current_calorie_count = 0 
        else:
            current_calorie_count += int(line.strip())
    
print(highest_calorie)
    