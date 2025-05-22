#https://www.acmicpc.net/problem/1826
#연료 채우기

import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./Greedy/1826/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())

GasStations = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
destination, fuel = map(int, sys.stdin.readline().strip().split())

GasStations = sorted(GasStations, key=lambda x: x[0])  
GasStations.append((destination, 0))

res = 0
prev_gs = []

for gs in GasStations:
  if fuel - gs[0] < 0:
    while prev_gs:
      fuel += abs(heapq.heappop(prev_gs))
      res += 1
      if fuel - gs[0] >= 0:
        break
  if len(prev_gs) == 0 and fuel - gs[0] < 0:
    res = -1
    break
  else:
    heapq.heappush(prev_gs, -gs[1])
print(res)