#https://www.acmicpc.net/problem/2513
#통학버스

import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./Greedy/2513/input.txt", "r").readlines()))

N, K, S = map(int, sys.stdin.readline().strip().split())
apts = [[] for dir in range(2)]
res = 0

for _ in range(N):
  apt_info = list(map(int, sys.stdin.readline().strip().split()))
  if apt_info[0] < S:
    heapq.heappush(apts[0], [(S - apt_info[0])*-1, apt_info[1]])
  else:
    heapq.heappush(apts[1], [(apt_info[0] - S)*-1, apt_info[1]])
    
#K 버스 정원
#S 학교 위치

bus = 0 
long_dist = 0
for dir in range(2):
  while apts[dir]:
    apt = heapq.heappop(apts[dir])
    
    if (K - bus) - abs(apt[1]) >= 0:
      bus += abs(apt[1])
      long_dist = max( long_dist, abs(apt[0]) )
    else:
      left = (abs(apt[1]) - (K - bus))
      bus += abs(apt[1]) - left
      heapq.heappush(apts[dir], [apt[0], left])
      long_dist = max( long_dist, abs(apt[0]) )
    
    if bus == K or len(apts[dir]) == 0:
      res += long_dist * 2
      long_dist = 0
      bus = 0
  
print(res)