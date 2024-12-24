#https://www.acmicpc.net/problem/1495
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1495/input.txt", "r").readlines()))

N, S, M = map(int, sys.stdin.readline().strip().split())
V_list = list(map(int, sys.stdin.readline().strip().split()))
dp_table = [[0 for _ in range(M)] for _ in range(N+1)]
dp_table[0][S] = S

for vIdx in range(1, N+1):
  for vol in range(M):
    