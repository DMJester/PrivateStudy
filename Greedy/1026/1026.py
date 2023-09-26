#https://www.acmicpc.net/problem/1026

import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
res = 0

for i in range(N):
    res += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
        
print(res)