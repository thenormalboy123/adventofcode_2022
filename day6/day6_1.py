if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    setof4 = ['','','',''] #need to ensure all these are unique 
    markercount = 0 #char counter 


    while 1:
        char = file1.read(1) #read file char by char 
        if markercount < 4: #fill up setof4 before doing comparison algorithm 
            setof4[markercount] = char
            markercount += 1
        else:
            if len(setof4) == len(set(setof4)): #if all char in setof4 are unique 
                print(markercount)
                break
            else: 
                setof4[markercount%4] = char #replace new char with the 1st char of the setof4 per input 
                markercount+=1 