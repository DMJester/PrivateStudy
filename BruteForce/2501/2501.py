#https://www.acmicpc.net/problem/2501
import sys

N, K = map(int, sys.stdin.readline().strip().split())
divisor_list = []
res = 0

for i in range(1, N+1):
    if N % i == 0:
        divisor_list.append(i)

if len(divisor_list) >= K:
    res = divisor_list[K-1]
    
print(res)