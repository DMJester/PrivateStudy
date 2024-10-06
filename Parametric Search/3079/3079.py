#https://www.acmicpc.net/problem/3079
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/3079/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
PassportControl = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = 0

min_time = 1
max_time = max(PassportControl) * M
while min_time <= max_time:
    set_time = ( min_time + max_time ) // 2
    kill_cnt = 0
    
    for t in PassportControl:
        kill_cnt += set_time // t
        if kill_cnt >= M:
            break
        
    if kill_cnt >= M:
        max_time = set_time - 1
        res = set_time
    else:
        min_time = set_time + 1
        

print(res)