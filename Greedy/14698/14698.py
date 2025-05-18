#https://www.acmicpc.net/problem/14698
#전생슬연구자

import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./Greedy/14698/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())

for idx in range(T):
  N = int(sys.stdin.readline().strip())
  Slimes = list(map(int, sys.stdin.readline().strip().split()))
  heapq.heapify(Slimes)
  step = []
  res = 1
  
  if N == 1:
    print(res)
    continue
  
  while len(Slimes) >= 2:
    Slime1 = heapq.heappop(Slimes)
    Slime2 = heapq.heappop(Slimes)
    
    Slimes.append( Slime1 * Slime2 )
    step.append(Slime1 * Slime2)
  for s in step:
    res *= s
  print(res % 1000000007)