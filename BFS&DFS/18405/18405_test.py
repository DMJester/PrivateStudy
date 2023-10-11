#https://www.acmicpc.net/problem/18405

import sys
from collections import deque

with open("input.txt", 'r') as f:
    N, K = map(int, f.readline().strip().split())
    tube_map = []
    virus_coordinate = []
    
    for i in range(N):
        tube_map.append(list(map(int, f.readline().strip().split())))
    
    S, X, Y = map(int, f.readline().strip().split())
    
    Q = deque()        
    
    for idx_x, val_x in enumerate(tube_map):
        for idx_y, val_y in enumerate(val_x):
            if val_y > 0:
                Q.append([idx_x, idx_y, val_y])
    
    stage = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    Q = deque(sorted(Q, key=lambda x:x[2]))
    while Q:
        if stage >= S: 
            break
        
        for i in range(len(Q)):
            x, y, virus = map(int, Q.popleft())
            
            for direction in range(4):
                mx = x + dx[direction]
                my = y + dy[direction]
                
                if mx >= 0 and mx <= N-1 and my >= 0 and my <= N-1:
                    if tube_map[mx][my] == 0 :
                        tube_map[mx][my] = virus
                        Q.append([mx, my, virus])
        stage += 1
    
    print(tube_map[X-1][Y-1])