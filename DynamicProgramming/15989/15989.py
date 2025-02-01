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
  
  
  
#1 = 0100 [1] 0 1 0 0
#2 = 0110 [1,1][2] 0 1 1 0
#3 = 0111 [1,1,1][2,1][3] 0 1 1 1
#4 = 0121 [1,1,1,1][2,1,1][2,2][3,1] 0 1 2 1 
#5 = 0122 [1,1,1,1,1] [2,1,1,1][2,2,1][2,3] [3,1,1][3,2] 0 1 2 2
#6 = 0133 [1,1,1,1,1,1][2,1,1,1,1][2,2,1,1][2,2,2][3,1,1,1][3,3] [3,2,1] 0 1 3 3
#7 = 0134 [1,1,1,1,1,1,1][2,1,1,1,1,1][2,2,1,1,1][2,2,2,1][3,1,1,1,1][3,3,1][3,2,1,1][3,2,2]