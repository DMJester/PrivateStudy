#https://www.acmicpc.net/problem/11047

import sys

N = int(sys.stdin.readline().strip())
P = list(map(int, sys.stdin.readline().strip().split()))
acc_sum = 0
res = 0

P.sort()

for i in P:
    acc_sum += i
    res += acc_sum

print(res)