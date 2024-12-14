#https://www.acmicpc.net/problem/1535
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1535/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
give = list(map(int, sys.stdin.readline().strip().split()))
take = list(map(int, sys.stdin.readline().strip().split()))

give.insert(0, 0)
take.insert(0, 0)

happy_table = [[0 for _ in range(100)] for __ in range(N+1)]

for y in range(1, N+1):
  for x in range(100):
    if give[y] <= x:
      prev = x-give[y]
      if prev < 0:
        prev = 0
      happy_table[y][x] = max( happy_table[y-1][x], happy_table[y-1][prev] + take[y] ) 
    else:
      happy_table[y][x] = happy_table[y-1][x]
      
print(happy_table[N][-1])