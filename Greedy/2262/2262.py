#https://www.acmicpc.net/problem/2262
#토너먼트만들기

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/2262/input.txt", "r").readlines()))

n = int(sys.stdin.readline().strip())
ranking = list(map(int, sys.stdin.readline().strip().split()))
res = 0

while ranking:
  now = ranking.index( max(ranking) )
  
  left = len(ranking)
  if left >= 2:
    if now == 0:
      res += ranking[now] - ranking[now+1]
    elif now == left-1:
      res += ranking[now] - ranking[now-1]
    else:
      res += min(ranking[now]-ranking[now-1], ranking[now]-ranking[now+1])
    ranking.pop(now)
  else:
    break
print(res) 