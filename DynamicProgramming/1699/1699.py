#https://www.acmicpc.net/problem/1699
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1699/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())

dp_table = [100001 for _ in range(N+1)]
dp_table[0] = 0
dp_table[1] = 1

for i in range(1, N+1):
  for p in range(1, N):
    square = p*p
    if square <= i:
      t = i - square
      if t < 0:
        t = 0
      dp_table[i] = min(dp_table[i], dp_table[i-(square)]+1)
    else:
      break
      
print(dp_table[N])