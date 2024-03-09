#https://www.acmicpc.net/problem/15686

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/15686/input.txt", "r").readlines()))

def dfs(depth, start):
    global res

    if depth == M:
        distance_list = []
        for home in home_list:
            distance = N*N*(N*2)
            for shop_number in shop_keep:
                this_dist = abs(home[0]-shop_list[shop_number][0]) + abs(home[1]-shop_list[shop_number][1])
                distance = min(distance, this_dist)
            distance_list.append(distance)
        res = min(res, sum(distance_list))
        return
    
    for idx in range(start, len(shop_list)):
        shop_keep[depth] = idx
        dfs(depth+1, idx+1)
        shop_keep[depth] = 0

N, M = map(int, sys.stdin.readline().strip().split())
city_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
home_list = []
shop_list = []
shop_keep = [0 for _ in range(M)]
res = N*N*(N*2)

for y, row in enumerate(city_map):
    for x, v in enumerate(row):
        if v == 1:
            home_list.append((y,x))
        if v == 2:
            shop_list.append((y,x))       

dfs(0, 0)

print(res)