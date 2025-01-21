#https://www.acmicpc.net/problem/9251
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/9251/input.txt", "r").readlines()))

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

dp_table = [[0 for _ in range(len(str1))] for __ in range(len(str2))]

for y in range(len(str1)):
  ny = y
  cnt = 0
  for x in range(len(str2)):
    if str1[ny] == str2[x]:
      