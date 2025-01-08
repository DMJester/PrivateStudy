#https://www.acmicpc.net/problem/1495
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1495/input.txt", "r").readlines()))

N, S, M = map(int, sys.stdin.readline().strip().split())
V_list = list(map(int, sys.stdin.readline().strip().split()))
dp_table = [[0, 0] for _ in range(N+1)]
dp_table[0] = [S, S]

for i in range(1, N+1):
  minus =  dp_table[i-1][0] - V_list[i-1]
  if minus >= 0:
    dp_table[i][0] = minus
  else:
    dp_table[i][0] = dp_table[i-1][0]
  
  plus = dp_table[i-1][1] + V_list[i-1]
  if plus <= M:
    dp_table[i][1] = plus
  else:
    dp_table[i][1] = dp_table[i-1][1]
  
print(dp_table)