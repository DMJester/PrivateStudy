#https://www.acmicpc.net/problem/1911
#흙길 보수하기

import sys
import math
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/1911/input.txt", "r").readlines()))

N, L = map(int, sys.stdin.readline().strip().split())
pools = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
pools.sort(key=lambda x:x[0])

res = 0

pool_start = 0
pool_end = 0
for p in pools:
  if pool_end != p[0]-1:
    plank -= (math.ceil((pool_end - pool_start) / L))
    pool_start = p[0]
    pool_end = p[1]
  else:
    pool_end = p[1]
res += math.ceil((pool_end - pool_start) / L)

print(res)