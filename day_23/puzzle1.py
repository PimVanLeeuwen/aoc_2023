import queue
import numpy as np
from sortedcontainers import SortedSet
import sys
np.set_printoptions(threshold=sys.maxsize)

input = open('input.txt', 'r')
output = open('output.txt', 'w')
inputLines = np.array([list(x) for x in [s.strip() for s in input.readlines()]])

print(len(inputLines[0]))

Q = queue.PriorityQueue()
Q.put((0,(0,1), set()))

while not Q.empty():
    l, coord, visited = Q.get()
    y,x = coord
    # print(l, y,x, inputLines[y][x])
    assert len(visited) == l
    if y == 140 and x == 139:
        print(l)
    visited_next = set(visited)
    visited_next.add((y,x))
    # print(visited_next)

    match inputLines[y][x]:
        case ">":
            d = (0,1) 
            if y+d[0] >= 0 and y+d[0] < 141 and x+d[1] >= 0 and x+d[1] < 141 and not (y+d[0],x+d[1]) in visited:   
                Q.put((l+1, (y+d[0],x+d[1]), visited_next))
        case "<":
            d = (0,-1) 
            if y+d[0] >= 0 and y+d[0] < 141 and x+d[1] >= 0 and x+d[1] < 141 and not (y+d[0],x+d[1]) in visited:   
                Q.put((l+1, (y+d[0],x+d[1]), visited_next))
        case "v":
            d = (1,0) 
            if y+d[0] >= 0 and y+d[0] < 141 and x+d[1] >= 0 and x+d[1] < 141 and not (y+d[0],x+d[1]) in visited:   
                Q.put((l+1, (y+d[0],x+d[1]), visited_next))
        case ".":
            for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                if y+d[0] >= 0 and y+d[0] < 141 and x+d[1] >= 0 and x+d[1] < 141 and (not (y+d[0],x+d[1]) in visited) and inputLines[y+d[0]][x+d[1]] in [".", "<", ">", "v"]:
                    Q.put((l+1, (y+d[0],x+d[1]), visited_next))

