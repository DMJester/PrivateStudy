#https://www.acmicpc.net/problem/5525
#IOIOI

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/5525/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

res = 0
pn = "IOI"
pn_len = len(pn)

now = 0
pn_cnt = 0
while now < M-pn_len+1:
  checkStr = S[now:now+pn_len]
  
  if pn == checkStr:
    pn_cnt += 1
    now += 2
  else:  
    if pn_cnt >= N:
      offset = pn_cnt - N
      res += 1 + offset
    pn_cnt = 0
    now += 1

if pn_cnt >= N:
  offset = pn_cnt - N
  res += 1 + offset

print(res)