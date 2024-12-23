#https://www.acmicpc.net/problem/1495
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1495/input.txt", "r").readlines()))

N, S, M = map(int, sys.stdin.readline().strip().split())
V_list = list(map(int, sys.stdin.readline().strip().split()))
dp_table = []

print(N, S, M)
print(V_list)