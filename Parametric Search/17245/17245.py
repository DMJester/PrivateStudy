#https://www.acmicpc.net/problem/17245
import sys
from io import StringIO
import math

sys.stdin = StringIO("".join(open("./Parametric Search/17245/input.txt").readlines()))

N = int(sys.stdin.readline().strip())
room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
computer_heights = sum(room, [])
computer_cnt = sum(computer_heights)
half = math.ceil(computer_cnt / 2) 
res = 0

low_time = 1
high_time = 10000000
while low_time <= high_time:
    if computer_cnt == 0:
        break
    set_time = ( low_time + high_time ) // 2
    on = 0

    for h in computer_heights:
        on += set_time if set_time - h <= 0 else h
        if on >= half:
            break
        
    if on >= half:
        high_time = set_time - 1
        res = set_time
    else:
        low_time = set_time + 1
        
print(res)
