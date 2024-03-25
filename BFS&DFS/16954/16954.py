import sys
from collections import deque 
from io import StringIO

sys.stdin = StringIO("".join(open("./16954/input.txt","r").readlines()))

board = [[char for char in sys.stdin.readline().strip()] for _ in range(8)]
board.insert(0, ['.','.','.','.','.','.','.','.'])
res = 0

direction = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, +1), (0, +1)]

Q = deque()
Q.append([0, 0])

while Q:
    nx, stage = Q.pop()
    
    if stage >= 9:
        res = 1
        break
    
    check_location = []
    next_location = []
    for i in range(2,0,-1):
        check_location.append(board[max(-9, -1*abs(i+stage))])
        next_location.append(board[max(-9, -1*abs(i+stage+1))])
        
    
    if check_location[1][nx] != '#':
        for dy, dx in direction:
            my = 1 + dy
            mx = nx + dx
            if mx >= 0 and mx <= 7 and my >= 0 and my <= 8:
                if check_location[my][mx] != '#' and next_location[my][mx] != '#':
                    Q.append([mx, stage+1])

print(res)