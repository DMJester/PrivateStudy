#https://www.acmicpc.net/problem/1495
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1495/input.txt", "r").readlines()))

N, S, M = map(int, sys.stdin.readline().strip().split())
V_list = list(map(int, sys.stdin.readline().strip().split()))
dp_table = [[False for _ in range(M+1)] for _ in range(N+1)]
dp_table[0][S] = True
res = -1

for vIdx in range(1, N+1):
  for vol in range(M+1):
    if dp_table[vIdx-1][vol]:
      minus = vol - V_list[vIdx-1]
      plus = vol + V_list[vIdx-1]
      
      if minus >= 0:
        dp_table[vIdx][minus] = True
        
      if plus <= M:
        dp_table[vIdx][plus] = True

for idx in range(M, 0, -1):
  if dp_table[-1][idx]:
    res = max(idx, res)
    break
  
print(res)
