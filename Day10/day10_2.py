total_signal_strength = 0 
CRT_map =  [['.' for x in range(40)] for y in range(6)]

def checkforticks(current_cycle, register_value):
    global total_signal_strength
    if current_cycle in [20,140,60,180,100,220]:
        print(f"At cycle {current_cycle}, signal strength is: {current_cycle * register_value}")
        total_signal_strength += (current_cycle*register_value)
    if current_cycle == 220:
        print(f"Final signal is {total_signal_strength}")
        exit()

def PrintScreen():
    global CRT_map
    for i in range(6):
        print()
        for j in range(40):
            print(CRT_map[i][j], end='')

def CheckSpritePosition(current_cycle, register_value):
    global CRT_map
    if abs(register_value-((current_cycle-1)%40)) <= 1: 
        CRT_map[int((current_cycle-1)/40)][(current_cycle-1)%40] = '#' #currentcycle starts at 1 

def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    current_cycle = 1
    register_value = 1  
    for line in Lines:
        instructions = line.strip().split()
        if current_cycle == 242: #Final time CheckSpritePosition should run is at pixel 240 (241-1), so should break at 242 
            break
        CheckSpritePosition(current_cycle, register_value)
        match instructions[0]:
            case 'noop':
                CheckSpritePosition(current_cycle, register_value)
                current_cycle += 1
            case 'addx':
                current_cycle += 1 
                CheckSpritePosition(current_cycle, register_value)
                current_cycle  += 1
                register_value += int(instructions[1])                
            case _: 
                print("no valid instuctions here")
    PrintScreen()




main()