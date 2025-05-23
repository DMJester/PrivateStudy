#https://www.acmicpc.net/problem/15990
#1, 2, 3 더하기 5

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/15990/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())
N_list = [int(sys.stdin.readline().strip()) for _ in range(T)]

max_number = max(N_list)
dp_table = [[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,1,1,1]]
dp_table += [[0 for __ in range(4)] for _ in range(4, max_number+1)]

for idx in range(4, max_number+1):
  dp_table[idx][1] += (dp_table[idx - 1][2] + dp_table[idx - 1][3]) % 1000000009
  dp_table[idx][2] += (dp_table[idx - 2][1] + dp_table[idx - 2][3]) % 1000000009
  dp_table[idx][3] += (dp_table[idx - 3][1] + dp_table[idx - 3][2]) % 1000000009
  
for N in N_list:
  print(sum(dp_table[N]) % 1000000009 )