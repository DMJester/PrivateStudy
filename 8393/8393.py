#https://www.acmicpc.net/problem/8393

import sys

N = int(sys.stdin.readline().strip())
res = 0

for x in range(1, N+1):
    res += x
    
print(res)