#https://www.acmicpc.net/problem/2792
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2792/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
jewels = [int(sys.stdin.readline().strip()) for _ in range(M)]
res = (1000000000 * M) + 1

left = 1
right = max(jewels)
while left <= right:
    set_ea = ( left + right ) // 2
    kid_cnt = 0
    envy = 0
    
    for j in jewels:
        if set_ea <= j:
            quotient, remain = divmod(j, set_ea)
        else:
            kid_cnt = 0
            envy = 0
            break
            
        kid_cnt += quotient
        envy = max(envy, set_ea)
        
        while remain >= 1:
            remain -= quotient
            envy += 1

    if kid_cnt >= N:
        left = set_ea + 1
        res = min(res, envy)
    else:
        right = set_ea - 1
print(res)
        