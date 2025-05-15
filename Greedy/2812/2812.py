#https://www.acmicpc.net/problem/2812
#크게만들기

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/2812/input.txt", "r").readlines()))

N, K = map(int, sys.stdin.readline().strip().split())
numbers = [ i for i in sys.stdin.readline().strip() ]
res = []
cnt = 0

for num in numbers:
  while cnt < K and res and res[-1] < num :
    res.pop()
    cnt += 1
  res.append(num)
  
while cnt < K:
  cnt += 1
  res.pop()
print("".join(res))