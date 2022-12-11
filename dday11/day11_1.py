Monkey_inventory = [[93,54,69,66,71],[89,51,80,66],[90,92,63,91,96,63,64],[65,77],[76,68,94],[86,65,66,97,73,83],[78],[89,57,59,61,87,55,55,88]]
inspection_count = [0,0,0,0,0,0,0,0]

def Monkey0():
    times_toinspect = len(Monkey_inventory[0])
    inspection_count[0] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[0][0] = int(int(Monkey_inventory[0][0] * 3) / 3) #operation and worry reduction 
        Monkey_inventory[7].append(Monkey_inventory[0][0]) if (Monkey_inventory[0][0] % 7 == 0) else Monkey_inventory[1].append(Monkey_inventory[0][0])
        Monkey_inventory[0].pop(0)

def Monkey1():
    times_toinspect = len(Monkey_inventory[1])
    inspection_count[1] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[1][0] = int(int(Monkey_inventory[1][0] * 17) / 3) #operation and worry reduction 
        Monkey_inventory[5].append(Monkey_inventory[1][0]) if (Monkey_inventory[1][0] % 19 == 0) else Monkey_inventory[7].append(Monkey_inventory[1][0])
        Monkey_inventory[1].pop(0)

def Monkey2():
    times_toinspect = len(Monkey_inventory[2])
    inspection_count[2] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[2][0] = int(int(Monkey_inventory[2][0] + 1) / 3) #operation and worry reduction 
        Monkey_inventory[4].append(Monkey_inventory[2][0]) if (Monkey_inventory[2][0] % 13 == 0) else Monkey_inventory[3].append(Monkey_inventory[2][0])
        Monkey_inventory[2].pop(0)

def Monkey3():
    times_toinspect = len(Monkey_inventory[3])
    inspection_count[3] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[3][0] = int(int(Monkey_inventory[3][0] + 2) / 3) #operation and worry reduction 
        Monkey_inventory[4].append(Monkey_inventory[3][0]) if (Monkey_inventory[3][0] % 3 == 0) else Monkey_inventory[6].append(Monkey_inventory[3][0])
        Monkey_inventory[3].pop(0)

def Monkey4():
    times_toinspect = len(Monkey_inventory[4])
    inspection_count[4] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[4][0] = int(int(Monkey_inventory[4][0] * Monkey_inventory[4][0]) / 3) #operation and worry reduction 
        Monkey_inventory[0].append(Monkey_inventory[4][0]) if (Monkey_inventory[4][0] % 2 == 0) else Monkey_inventory[6].append(Monkey_inventory[4][0])
        Monkey_inventory[4].pop(0)

def Monkey5():
    times_toinspect = len(Monkey_inventory[5])
    inspection_count[5] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[5][0] = int(int(Monkey_inventory[5][0] + 8) / 3) #operation and worry reduction 
        Monkey_inventory[2].append(Monkey_inventory[5][0]) if (Monkey_inventory[5][0] % 11 == 0) else Monkey_inventory[3].append(Monkey_inventory[5][0])
        Monkey_inventory[5].pop(0)

def Monkey6():
    times_toinspect = len(Monkey_inventory[6])
    inspection_count[6] += times_toinspect
    for i in range(times_toinspect):
        Monkey_inventory[6][0] = int(int(Monkey_inventory[6][0] + 6) / 3) #operation and worry reduction 
        Monkey_inventory[0].append(Monkey_inventory[6][0]) if (Monkey_inventory[6][0] % 17 == 0) else Monkey_inventory[1].append(Monkey_inventory[6][0])
        Monkey_inventory[6].pop(0)

def Monkey7():
    times_toinspect = len(Monkey_inventory[7])
    inspection_count[7] += times_toinspect
    for _ in range(times_toinspect):
        Monkey_inventory[7][0] = int(int(Monkey_inventory[7][0] + 7) / 3) #operation and worry reduction 
        Monkey_inventory[2].append(Monkey_inventory[7][0]) if (Monkey_inventory[7][0] % 5 == 0) else Monkey_inventory[5].append(Monkey_inventory[7][0])
        Monkey_inventory[7].pop(0)




def main():

    for _ in range(20):
        Monkey0()
        Monkey1()
        Monkey2()
        Monkey3()
        Monkey4()
        Monkey5()
        Monkey6()
        Monkey7()
    inspection_count.sort()
    print(inspection_count[6] * inspection_count[7]) #print product of largest 2 counts 

main()