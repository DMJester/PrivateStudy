#https://www.acmicpc.net/problem/14502

import sys
from collections import deque

def reinforce_wall(input_map, wall_cnt, res):
    if wall_cnt >= 3:
        res.append( int(spread_virus(input_map)) )
        return

    for y in range(N):
        for x in range(M):
            if input_map[y][x] == 0:
                input_map[y][x] = 1
                reinforce_wall(input_map, wall_cnt+1, res)
                input_map[y][x] = 0
    
def spread_virus(input_map):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    Q = deque()        
    test_map = [item[:] for item in input_map]
    
    for idx_y, val_y in enumerate(test_map):
        for idx_x, val_x in enumerate(val_y):
            if val_x == 2:
                Q.append([idx_x, idx_y, val_x])
    
    while Q:
        x, y, virus = map(int, Q.popleft())
        
        for direction in range(4):
            mx = x + dx[direction]
            my = y + dy[direction]
            
            if mx >= 0 and mx <= M-1 and my >= 0 and my <= N-1:
                if test_map[my][mx] == 0:
                    test_map[my][mx] = virus
                    Q.append([mx, my, virus])

    cnt = 0
    for col in test_map:
        cnt += col.count(0) 
    return cnt

with open("./BFS&DFS/14502/input.txt", 'r') as f:
    N, M = map(int, f.readline().strip().split())
    wall_map = []
    res = []
    
    for y in range(N):
        wall_map.append(list(map(int, f.readline().strip().split())))
        
    reinforce_wall(wall_map, 0, res)
    print(max(res))
    