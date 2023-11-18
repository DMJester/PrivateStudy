#https://www.acmicpc.net/submit/2468
import sys
from collections import deque

def find_area(rainfall):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    tmp_map = [item[:] for item in height_map]
    visit_map = [[0 for _ in range(N)] for __ in range(N)]
    area_cnt = 0
    
    Q = deque()
    for y in range(N):
        for x in range(N):
            tmp_map[y][x] -= rainfall
            if tmp_map[y][x] <= 0:
                visit_map[y][x] = 1
                
    for y in range(N):
        for x in range(N):
            if visit_map[y][x] == 0:
                area_cnt += 1
                Q.append((x, y))
                while Q:
                    q_x, q_y = map(int, Q.popleft())
                    if visit_map[q_y][q_x] == 1:
                        continue
                    else :
                        visit_map[q_y][q_x] = 1
                        
                    for direction in range(4):
                        mx = q_x + dx[direction]
                        my = q_y + dy[direction]
                        if mx >= 0 and mx <= N-1 and my >= 0 and my <= N-1:
                            if visit_map[my][mx] == 0:
                                Q.append((mx, my))
    return area_cnt
            
with open("./Greedy/2468/input.txt") as f:
    N = int(f.readline().strip())
    height_map = []
    height_list = []
    res = 1
    
    for i in range(N):
        height_map.append(list(map(int, f.readline().strip().split())))

    height_list = sum(height_map, [])
    height_list = list(set(height_list))
    
    for rainfall in height_list:
        res = max(res, find_area(rainfall))
    
    print(res)