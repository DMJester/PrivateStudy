#https://www.acmicpc.net/problem/1793
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1793/input.txt", "r").readlines()))
nlist = []
n = sys.stdin.readline().strip()
while n:
  nlist.append(int(n))
  n = sys.stdin.readline().strip()

dp_table = [[0,0] for _ in range(251)]
dp_table[0][0] = 1
dp_table[1][0] = 1

for i in range(2, 251):
  dp_table[i][0] = sum(dp_table[i-1])
  dp_table[i][1] = dp_table[i-1][0] * 2

for idx in nlist:
  print(sum(dp_table[idx]))