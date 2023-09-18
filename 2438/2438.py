#https://www.acmicpc.net/problem/2438

import sys

N = int(sys.stdin.readline().strip())

for x in range(1, 10):
    print("{} * {} = {}".format(N, x, N*x))