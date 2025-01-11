#https://www.acmicpc.net/problem/2193
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/2193/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
dp_table = [[0,0], [0, 1], [1, 0]]
dp_table += [[0,0] for _ in range(N - 2)]

for i in range(3, N+1):
  dp_table[i][0] = dp_table[i-1][0] + dp_table[i-1][1]
  dp_table[i][1] = dp_table[i-1][0]  
  
print(sum(dp_table[N]))   