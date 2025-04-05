#https://www.acmicpc.net/problem/1781
#컵라면

import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./1781/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
iq = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
iq.sort(key=lambda x: x[0])

can_solved = []
for p in iq:
  heapq.heappush(can_solved, p[1])
  if len(can_solved) > p[0]:
    heapq.heappop(can_solved)

print(sum(can_solved))