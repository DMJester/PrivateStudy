#https://www.acmicpc.net/problem/2212
#센서

import sys
from io import StringIO

#sys.stdin = StringIO("".join(open("./2212/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
sensors = sorted(set(map(int, sys.stdin.readline().strip().split())))
dists = []

res = 0
if K >= N :
  print(res)
else:
  for i in range(1, len(sensors)):
    dists.append(sensors[i] - sensors[i-1])
  dists = sorted(dists)

  print(sum(dists[0:len(dists)-(K-1)]))

"""
{1, 3, 6, 7, 9}
  2  3  1  2
   0  0  0  0  0 

{3, 6, 7, 8, 10, 12, 14, 15, 18, 20}
  3  1  1  2   2   2   1   3   2
"""