import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/2003/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
res = 0

for idx, v in enumerate(A):
    tmp = 0
    for i in range(idx, N):
        tmp += A[i]
        if tmp == M:
            res += 1
            tmp = 0
            break
        elif tmp > M:
            tmp = 0
            break

print(res)