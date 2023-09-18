#https://www.acmicpc.net/problem/2741

import sys

T = int(sys.stdin.readline().strip())
res = [ 0 for i in range(T)]

for i in range(T):
    res[i] = sum(map(int, sys.stdin.readline().strip().split()))
    
for r in res:
    print(r)