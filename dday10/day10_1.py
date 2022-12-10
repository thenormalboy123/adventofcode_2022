total_signal_strength = 0 

def checkforticks(current_cycle, register_value):
    global total_signal_strength
    if current_cycle in [20,140,60,180,100,220]:
        print(f"At cycle {current_cycle}, signal strength is: {current_cycle * register_value}")
        total_signal_strength += (current_cycle*register_value)
    if current_cycle == 220:
        print(f"Final signal is {total_signal_strength}")
        exit()


def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    current_cycle = 1
    register_value = 1  
    for line in Lines:
        instructions = line.strip().split()
        checkforticks(current_cycle, register_value)
        match instructions[0]:
            case 'noop':
                current_cycle += 1
            case 'addx':
                current_cycle += 1 
                checkforticks(current_cycle, register_value)
                current_cycle  += 1
                register_value += int(instructions[1])                
            case _: 
                print("no valid instuctions here")

main()