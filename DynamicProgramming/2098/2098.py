#https://www.acmicpc.net/problem/2098
#외판원 순회
import sys
from io import StringIO
import itertools

sys.stdin = StringIO("".join(open("./DynamicProgramming/2098/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

INF = 16000001
dp = [[INF] * (1<<N) for _ in range(N)]

for d in dp:
  print(d)
  
  
'''
1
10
100
1000
10000
'''