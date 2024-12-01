#https://www.acmicpc.net/problem/16395
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/16395/input.txt").readlines()))

n, k = map(int, sys.stdin.readline().strip().split())
ps_triangle = [[0 for _ in range(n)] for __ in range(n)]
ps_triangle[0][0] = 1

for y in range(1, n):
  up_x = 0
  for x in range(y+1):
    if x == 0:
      ps_triangle[y][0] = 1
      continue
    elif x == y:
      ps_triangle[y][x] = 1
      break
    
    else:
      if up_x < y:
        ps_triangle[y][x] = ps_triangle[y-1][up_x] + ps_triangle[y-1][up_x+1]
        up_x += 1
      else:
        ps_triangle[y][x] = 1

print(ps_triangle[n-1][k-1])