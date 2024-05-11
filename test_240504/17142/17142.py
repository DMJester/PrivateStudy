import sys
from io import StringIO
from collections import deque

sys.stdin = StringIO("".join(open("./test_240504/17142/input.txt").readlines()))

def spread_virus(input_map):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    spread_sec = -1
    left_space = space_cnt
    
    Q = deque()        
    test_map = [item[:] for item in input_map]
    
    for x, y, s in virus_comb:
        Q.append([x, y, s])
        test_map[y][x] = 4
    
    while Q:
        x, y, sec = map(int, Q.popleft())
        spread_sec = max(spread_sec, sec)
        
        for direction in range(4):
            mx = x + dx[direction]
            my = y + dy[direction]
            
            if mx >= 0 and mx <= N-1 and my >= 0 and my <= N-1:
                if test_map[my][mx] == 0 or test_map[my][mx] == 2:
                    if left_space <= 0:
                        break
                    else:
                        Q.append([mx, my, sec+1])
                        if test_map[my][mx] == 0:
                            left_space -= 1
                        test_map[my][mx] = 4
    
    if left_space <= 0:
        return spread_sec
    else:
        return 2500

def dfs(depth, start):
    global virus_comb
    global res
    
    if depth == M:
        res = min(res, spread_virus(lab_map))
        return
    
    for i in range(start, len(virus_loc)):
        if virus_use[i] == False:
            virus_use[i] = True
            virus_comb.append(virus_loc[i])
            
            dfs(depth+1, i)
            
            virus_use[i] = False
            virus_comb.pop()

N, M = map(int, sys.stdin.readline().strip().split())
lab_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
virus_loc = []
virus_use = []
virus_comb = []
space_cnt = 0

res = 2500

for y, yv in enumerate(lab_map):
    for x, xv in enumerate(yv):
        if xv == 2:
            virus_loc.append((x, y, 0))
            virus_use.append(False)
        if xv == 0:
            space_cnt += 1
            
dfs(0, 0)

if res == 2500:
    print(-1)
else:
    print(res)
