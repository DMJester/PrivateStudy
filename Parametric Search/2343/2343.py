#https://www.acmicpc.net/problem/2343
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2343/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
course = list(map(int, sys.stdin.readline().strip().split()))
course.append(0)
res = 0

min_time = 1
max_time = (100000*10000)+1
while min_time <= max_time:
    set_time = (min_time+max_time) // 2
    check_time = 0
    disc_cnt = 0
    
    for time in course:
        check_time += time
        if check_time > set_time:
            disc_cnt += 1
            check_time = 0
            check_time += time
        elif check_time == set_time:
            disc_cnt += 1
            check_time = 0
        
    if disc_cnt >= M:
        min_time = set_time + 1
        res = set_time
    else:
        max_time = set_time - 1
            
print(res)