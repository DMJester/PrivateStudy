#https://www.acmicpc.net/problem/2792
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/18113/input.txt", "r").readlines()))

N, K, M = map(int, sys.stdin.readline().strip().split())
GIMBAPS = []
res = -1

for _ in range(N):
    g = int(sys.stdin.readline().strip())
    
    if g - ( K * 2 ) >= 1:
        GIMBAPS.append(g - (K*2))
    elif g - K >= 1 and g - ( K * 2 ) != 0:
        GIMBAPS.append(g - K)

if len(GIMBAPS) >= 1:
    left = 1
    right = max(GIMBAPS)
    while left <= right:
        p_length = ( left + right ) // 2
        p_cnt = 0
        
        for gb in GIMBAPS:
            p_cnt += gb // p_length
        
        if p_cnt >= M:
            left = p_length + 1
            res = max(res, p_length)
        else:
            right = p_length - 1
            
print(res)