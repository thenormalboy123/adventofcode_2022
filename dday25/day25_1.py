def Get_SNAFU(value):
    list_of_digits = []
    result = value
    returnvalue = ''
    for i in range(50): #arbitrary number, 5^50 is almost 1E35, we assume number will not be that big 
        if result % (5**(i+1)) == 0: # next least significant digit = '0'
            list_of_digits.append('0')
        elif (result+(5**i)) % (5**(i+1)) == 0: # next least significant digit = '-'
            result+=(5**i)
            list_of_digits.append('-')
        elif (result+((5**i))*-1) % (5**(i+1)) == 0: # next least significant digit = '+'
            result-=(5**i)
            list_of_digits.append('1')
        elif (result+((5**i)*2)) % (5**(i+1)) == 0: # next least significant digit = '='
            result+=((5**i)*2)
            list_of_digits.append('=')
        elif (result+((5**i))*-2) % (5**(i+1)) == 0: # next least significant digit = '2'
            result-=((5**i)*2)
            list_of_digits.append('2')
        else: # catching error just in case 
            print("Error, something happened")
        if result == 0:
            break
    for a in range(len(list_of_digits)):
        returnvalue += list_of_digits[len(list_of_digits) - a - 1]
    return returnvalue

def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    sum = 0 

    for line in Lines: 
        line = line.strip()
        value_in_decimal = 0 
        for digit in range(len(line)):       
            match line[len(line) - digit - 1]:
                case '1': 
                    value_in_decimal += 5**(digit)
                case '2': 
                    value_in_decimal += (5**digit) * 2 
                case '-': 
                    value_in_decimal += 5**(digit) * -1
                case '=': 
                    value_in_decimal += (5**(digit) * -2)
                case _: 
                    pass
        sum += value_in_decimal

    print(Get_SNAFU(sum))

main()