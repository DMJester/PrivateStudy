#https://www.acmicpc.net/problem/11399

import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = []
res = 0

for i in range(N):
    val = int(sys.stdin.readline().strip())
    if val > K:
        continue
    else :
        A.append(val)

A.reverse()
    
for val in A:
    res += int(K / val)
    K = K % val

print(res)