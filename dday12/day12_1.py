from collections import deque

AB = "abcdefghijklmnopqrstuvwxyz" #could have use ord but sure 

def bfs(map, pos):
    w, h = len(map[0]), len(map)
    q = deque([[pos]])
    seen = set([pos])
    while q:
        path = q.popleft()
        x, y = path[-1]
        if map[y][x] == "E":
            return path
        e = AB.index(map[y][x])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in seen:
                e2 = AB.index(map[y2][x2]) if map[y2][x2] != "E" else 26
                if e2 <= e + 1:
                    q.append(path + [(x2, y2)])
                    seen.add((x2, y2))

def main():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    num_rows = len(Lines)
    num_col = len(Lines[0].strip())
    map =  [[0 for x in range(num_col)] for y in range(num_rows)]    
    file1.seek(0)
    current_line = 0 

    #write to 2D array 
    for line in Lines:
        line_edited = line.strip()
        map[current_line] = list(line_edited)
        current_line += 1

    #find S and E 
    y, x = [(n, r.index("S")) for n, r in enumerate(map) if "S" in r][0]
    y2, x2 = [(n, r.index("E")) for n, r in enumerate(map) if "E" in r][0]
    map[y][x] = 'a'
    print(f"Part 1: {len(bfs(map, (x, y))) - 1}")
    #start dijkstra shortest path algo 
    

main()