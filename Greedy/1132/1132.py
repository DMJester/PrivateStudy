#https://www.acmicpc.net/problem/1132
#합

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/1132/input.txt", "r").readlines()))

N = int(sys.stdin.readline())

print(N)