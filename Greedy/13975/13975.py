#https://www.acmicpc.net/problem/13975
#파일 합치기 3

import sys
from io import StringIO

import heapq

sys.stdin = StringIO("".join(open("./Greedy/13975/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())
F = []

for idx in range(T):
  int(sys.stdin.readline().strip())
  F = list(map(int, sys.stdin.readline().strip().split()))

  heapq.heapify(F)
  res = 0

  while F:
    if len(F) >= 2:
      number1 = heapq.heappop(F)
      number2 = heapq.heappop(F)

      sum_number = number1 + number2
      heapq.heappush(F, sum_number)
      res += sum_number
    else:
      break

  print(res)
