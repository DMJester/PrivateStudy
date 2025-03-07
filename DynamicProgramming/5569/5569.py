#https://www.acmicpc.net/problem/5569
#출근 경로

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/5569/input.txt", "r").readlines()))

w, h = map(int, sys.stdin.readline().strip().split())
dp = [[[0,0,0,0] for _ in range(w-1)] for _ in range(h-1)]

for x in range(1, w-1):
  dp[0][x] = (1,0,0,1)

for y in range(1, h-1):
  dp[y][0] = (0,1,1,0)

#RO RX DO DX
for y in range(1, h-1):
  for x in range(1, w-1):
    dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][1]
    dp[y][x][1] = dp[y][x-1][2]
    dp[y][x][2] = dp[y-1][x][2] + dp[y-1][x][3]
    dp[y][x][3] = dp[y-1][x][0]
    
print(sum(dp[-1][-1]) % 100000)