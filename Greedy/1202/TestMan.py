import heapq
import sys
import random

from collections import deque
from io import StringIO

def ran(_in):
  global ans;sys.stdin = StringIO(_in);N, K = map(int, sys.stdin.readline().strip().split());MV = deque(sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)], key = lambda x: x[0]));C = deque(sorted([int(sys.stdin.readline().strip()) for _ in range(K)]));q = [];ans = 0
  while (MV and C):
    while MV:
      if (C[0] < MV[0][0]): break
      m, v = MV.popleft();heapq.heappush(q, -v)
    ans += -heapq.heappop(q) if q else 0; C.popleft()
  while (q and C): ans += -heapq.heappop(q);C.popleft()
  return ans

def dmj(_in):
  sys.stdin = StringIO(_in)

  N, K = map(int, sys.stdin.readline().strip().split())
  jewels = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
  pouchs = [int(sys.stdin.readline().strip()) for _ in range(K)]
  res = 0

  jewels.sort(key=lambda x:x[0])
  pouchs.sort(reverse=False)
  heap = []

  idx = 0
  for pouch in pouchs:
      while idx < N and pouch >= jewels[idx][0]:
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1
      if heap:
        res += -heapq.heappop(heap)

  return res
  
while True:
    N, K = [random.randint(1, 3), random.randint(1, 3)]
    MV = "\n".join([f"{random.randint(1, 10)} {random.randint(1, 10)}" for _ in range(N)])
    C = "\n".join([f"{random.randint(1, 10)}" for _ in range(K)])

    _in = f"{N} {K}\n{MV}\n{C}"

    a = ran(_in)
    b = dmj(_in)

    if (a != b):
        print(f"{a} != {b}")
        print(_in)
        break