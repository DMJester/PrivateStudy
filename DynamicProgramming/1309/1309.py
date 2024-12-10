#https://www.acmicpc.net/problem/1309
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1309/input.txt", "r").readlines()))

N = int(sys.stdin.readline())
dp_table = [[0, 0] for _ in range(N)]
dp_table[0][0] = 1
dp_table[0][1] = 1

for i in range(1, N+1):
  dp_table[i][0] = sum(dp_table[i-1])
  dp_table[i][1] = 

print(dp_table[-1][0] + (dp_table[-1][1] * 2))