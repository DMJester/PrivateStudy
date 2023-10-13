#https://www.acmicpc.net/problem/1789

import sys

S = int(sys.stdin.readline().strip())
res = 0

sum = 0
N = 1
while 1:
    sum += N
    if sum <= S:
        res = N
    else:
        break;
    N += 1

print(res)