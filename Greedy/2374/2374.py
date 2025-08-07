#https://www.acmicpc.net/problem/2374
#같은 수로 만들기

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/2374/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
A_List = [int(sys.stdin.readline().strip()) for _ in range(N)]

for idx in N:
  A_List