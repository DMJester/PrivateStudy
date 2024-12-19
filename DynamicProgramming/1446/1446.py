#https://www.acmicpc.net/problem/1446
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1446/input.txt", "r").readlines()))

N, D = map(int, sys.stdin.readline().strip().split())
shortcuts = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ] 
running_in_the_90s = [i for i in range(D+1)]

for sp, ep, dist in shortcuts:
  for now in range(ep, D+1):
      if now == ep:
        running_in_the_90s[ep] = min(running_in_the_90s[ep], running_in_the_90s[sp]+dist)
      else:
        running_in_the_90s[now] = min(running_in_the_90s[now], running_in_the_90s[now-1] + 1)
      
print(running_in_the_90s[D])