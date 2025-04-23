#https://www.acmicpc.net/problem/2457
#공주님의 정원

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/2457/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
flowers = []
res = 0

for idx in range(N):
  sm, sd, em, ed = map(int, sys.stdin.readline().strip().split())
  flowers.append( ( (sm * 100) + sd, (em * 100) + ed ) )
flowers.sort(key=lambda x: (x[0], x[1]))

idx = 0
last_date = 301
prev_date = 0
for flower in flowers:
  if flower[0] > last_date:
    res += 1
    last_date = prev_date
    if last_date >= 1201:
      break

  if flower[0] <= last_date:
    if flower[1] > prev_date:
      prev_date = flower[1]

if prev_date > last_date:
  res += 1
  last_date = prev_date

if last_date >= 1201:
  print(res)
else:
  print(0)

'''
1201
101, 531
101, 630
515, 831
610, 1210

101 -> 630 -> 831 -> 1210

101 630 remove; last_date 630
101 531
515 831

610 1210
'''