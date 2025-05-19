#https://www.acmicpc.net/problem/1826
#연료 채우기

import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./Greedy/1826/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())

GasStations = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
GasStations = sorted(GasStations, key=lambda x: x[0])  

L, P = map(int, sys.stdin.readline().strip().split())
GasStations.append((L, 0))

res = 0
now_loc = 0
next_gss = []
for gs in GasStations:
  if gs[0]-now_loc <= P:
    heapq.heappush(next_gss, (-1*gs[1], gs[0]))
  else:
    stop_station = heapq.heappop(next_gss)
    P = (P - (stop_station[1]-now_loc)) + abs(stop_station[0])
    now_loc = stop_station[1]
    heapq.heappush(next_gss, (-1*gs[1], gs[0]))
    res += 1
print(res)
      