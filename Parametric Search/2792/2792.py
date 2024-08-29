#https://www.acmicpc.net/problem/2792
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2792/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
jewels = [int(sys.stdin.readline().strip()) for _ in range(M)]
max_cnt = max(jewels)
res = max_cnt

left = 1
right = max_cnt
while left <= right:
    set_ea = ( left + right ) // 2
    kid_cnt = 0
    
    for j in jewels:
        quotient, remain = divmod(j, set_ea)
        kid_cnt += quotient
        
        if remain >= 1:
            kid_cnt += 1

    if kid_cnt > N:
        left = set_ea + 1
    else:
        right = set_ea - 1
        res = set_ea
        
print(res)