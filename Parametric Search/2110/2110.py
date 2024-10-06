#https://www.acmicpc.net/problem/2110
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2110/input.txt", "r").readlines()))

N, C = map(int, sys.stdin.readline().strip().split())
house_loc = [int(sys.stdin.readline().strip()) for _ in range(N)]
house_loc.sort()
res = 0

min_dist = 1
max_dist = 1000000000
while min_dist <= max_dist:
    set_dist = ( min_dist + max_dist) // 2
    base = 0
    set_cnt = 0
    
    for idx, loc in enumerate(house_loc):
        if idx == 0:
            base = loc
            set_cnt += 1
        else:
            if (loc - base) >= set_dist:
                base = loc
                set_cnt += 1
    
    if set_cnt >= C:
        min_dist = set_dist + 1
        res = set_dist
    else:
        max_dist = set_dist - 1

print(res)