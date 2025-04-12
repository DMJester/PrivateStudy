#https://www.acmicpc.net/problem/2109
#순회강연

import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./Greedy/2109/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
iq = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
for idx in range(N):
  iq[idx] = [iq[idx][1], iq[idx][0]]
iq.sort(key=lambda x: x[0])

can_solved = []
for p in iq:
  heapq.heappush(can_solved, p[1])
  if len(can_solved) > p[0]:
    heapq.heappop(can_solved)

print(sum(can_solved))