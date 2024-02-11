import sys
from io import StringIO
from collections import deque

sys.stdin = StringIO("".join(open("./BruteForce/16197/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
board = [[s for s in sys.stdin.readline().strip()] for _ in range(N)]
res = -1
mx = [0, 0]
my = [0, 0]
sel = 0

nx = [0, 0]
ny = [0, 0]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for y, row in enumerate(board):
    for x, val in enumerate(row):
        if val == 'o':
            mx[sel] = x
            my[sel] = y
            sel += 1

Q = deque()
Q.append( [ ( mx[0], my[0] ), ( mx[1], my[1] ), 0 ] )

while Q:
    fall_cnt = 0
    check_cnt = 0
    locs = Q.popleft()
    
    for direction in range(4):
        fall_cnt = 0
        check_cnt = 0
        
        mx[0] = locs[0][0]
        my[0] = locs[0][1]
        nx[0] = mx[0]
        ny[0] = my[0]
        
        mx[1] = locs[1][0]
        my[1] = locs[1][1]
        nx[1] = mx[1]
        ny[1] = my[1]
        
        mx[0] += dx[direction]
        my[0] += dy[direction]
        
        mx[1] += dx[direction]
        my[1] += dy[direction]
        
        if mx[0] >= 0 and mx[0] < M and my[0] >= 0 and my[0] < N:
            if board[my[0]][mx[0]] != '#':
                nx[0] = mx[0]
                ny[0] = my[0]
                check_cnt += 1
        else:
            fall_cnt += 1
            
        if mx[1] >= 0 and mx[1] < M and my[1] >= 0 and my[1] < N:
            if board[my[1]][mx[1]] != '#':
                nx[1] = mx[1]
                ny[1] = my[1]
                check_cnt += 1
        else:
            fall_cnt += 1
            
        if fall_cnt == 1:
            Q.clear()
            res = locs[2] + 1
            break
        
        if locs[2] >= 10:
            Q.clear()
            break
        
        if check_cnt >= 1:
            Q.append([ ( nx[0], ny[0] ), ( nx[1], ny[1] ), locs[2] + 1 ])
    
print(res)