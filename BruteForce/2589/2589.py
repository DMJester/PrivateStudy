#https://www.acmicpc.net/problem/2589
import sys
from collections import deque

def find_treasure():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    distance = 0
    
    Q = deque()
    for sy in range(y_max):
        for sx in range(x_max):
            visit_map = [[0 for _ in range(x_max)] for __ in range(y_max)]
            if visit_map[sy][sx] == 0 and treasure_map[sy][sx] == 'L':
                Q.append((sx,sy,0))
                
            while Q:
                qx, qy, current_cnt = Q.popleft()
                if visit_map[qy][qx] == 1 or treasure_map[sy][sx] == 'W':
                    continue
                visit_map[qy][qx] = 1
                distance = max(distance, current_cnt)
                    
                for direction in range(4):
                    mx = qx + dx[direction]
                    my = qy + dy[direction]
                    if mx >= 0 and mx <= x_max-1 and my >= 0 and my <= y_max-1:
                        if visit_map[my][mx] == 0 and treasure_map[my][mx] == 'L':
                            Q.append((mx, my, current_cnt+1))
    return distance

y_max, x_max = map(int, sys.stdin.readline().strip().split())
treasure_map = []
res = 0

for y in range(y_max):
    treasure_map.append(list(sys.stdin.readline().strip()))

print(find_treasure())