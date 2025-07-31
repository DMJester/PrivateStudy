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

now = 0
for p in pools:
  now = max(p[0], now)
  plank = (math.ceil((p[1] - now)/L))
  now += plank * L
  res += plank
print(res)