#https://www.acmicpc.net/problem/15988
#1,2,3 더하기 3

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/15988/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())
N_list = [int(sys.stdin.readline().strip()) for _ in range(T)]

max_number = max(N_list)
dp_table = [0, 1, 2, 4]
dp_table += [0 for _ in range(4, max_number+1)]

for idx in range(4, max_number+1):
  dp_table[idx] = (dp_table[idx - 1] + dp_table[idx - 2] + dp_table[idx - 3]) % 1000000009
  
for N in N_list:
  print( dp_table[N] % 1000000009 )