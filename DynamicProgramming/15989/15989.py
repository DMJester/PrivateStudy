#https://www.acmicpc.net/problem/15989
#1, 2, 3 더하기 4

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/15989/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())
N_list = [int(sys.stdin.readline().strip()) for _ in range(T)]

max_number = max(N_list)
dp_table = [[0,0,0,0],[0,1,0,0],[0,1,1,0],[0,1,1,1]]
dp_table += [[0 for __ in range(4)] for _ in range(4, max_number+1)]

for idx in range(4, max_number+1):
  for n in range(1, 4):
    if n == 1:
      dp_table[idx][1] = 1
    elif n == 2:
      dp_table[idx][2] += sum( dp_table[idx - 2] )
    elif n == 3:
      dp_table[idx][3] += dp_table[idx - 3][1] + dp_table[idx - 3][3]
  
for N in N_list:
  print(sum(dp_table[N]))