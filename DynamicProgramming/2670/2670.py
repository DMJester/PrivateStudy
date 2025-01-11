#https://www.acmicpc.net/problem/2670
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/2670/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
N_list = [float(sys.stdin.readline().strip()) for _ in range(N)]
dp_table = [0] + N_list[:]

for i in range(N):
  dp_table[i] = max(dp_table[i], dp_table[i-1] * dp_table[i])
  
print("{:.3f}".format(round(max(dp_table), 3)))