#https://www.acmicpc.net/problem/9252
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/9252/input.txt", "r").readlines()))

str1 = "1"
str2 = "2"
str1 += sys.stdin.readline().strip()
str2 += sys.stdin.readline().strip()

dp_table = [[0 for _ in range(len(str2))] for __ in range(len(str1))]

for y in range(1, len(str1)):
  for x in range(1, len(str2)):
    if str1[y] == str2[x]:
      dp_table[y][x] = dp_table[y-1][x-1] + 1
    else:
      dp_table[y][x] = max(dp_table[y][x-1], dp_table[y-1][x])
      
print(dp_table[-1][-1])