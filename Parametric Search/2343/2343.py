#https://www.acmicpc.net/problem/2343
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2343/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
course = list(map(int, sys.stdin.readline().strip().split()))
res = 0

min_time = max(course)
max_time = sum(course)
while min_time <= max_time:
    set_time = (min_time+max_time) // 2
    highest_time = 0
    check_time = 0
    disc_cnt = 0

    for time in course:
        check_time += time
        if check_time > set_time:
            disc_cnt += 1
            highest_time = max(highest_time, check_time-time)
            check_time = time
        elif check_time == set_time:
            disc_cnt += 1
            highest_time = max(highest_time, check_time)
            check_time = 0
    
    if check_time >= 1:
        disc_cnt += 1
    
    if disc_cnt <= M:
        max_time = set_time - 1
        res = highest_time
    else:
        min_time = set_time + 1
            
print(res)