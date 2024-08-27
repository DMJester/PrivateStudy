#https://www.acmicpc.net/problem/2792
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2792/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
jewels = [int(sys.stdin.readline().strip()) for _ in range(M)]

left = 1
right = 1000000000 * M
while left <= right:
    set_ea = ( left + right ) // 2
    remain_sum = 0
    
    for j in jewels:
        