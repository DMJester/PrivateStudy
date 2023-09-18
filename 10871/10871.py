#https://www.acmicpc.net/problem/10871

import sys

N, X = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
res = []

for n in A:
    if n < X:
        res.append(n)
        
print(*res)