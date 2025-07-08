#https://www.acmicpc.net/problem/25381
#ABBC

import sys
from io import StringIO
from collections import deque

sys.stdin = StringIO("".join(open("./Greedy/25381/input.txt", "r").readlines()))

S = sys.stdin.readline().strip()
alpha = [ deque() for _ in range(3) ]
res = 0

A = 0
B = 1
C = 2
for idx, s in enumerate(S):
  alpha[eval(s)].append( idx )
  
now_alpha = C
while now_alpha >= 1:
  for now_idx in alpha[ now_alpha ]:
    if len(alpha[ now_alpha - 1 ]) >= 1 and alpha[ now_alpha - 1 ][0] < now_idx:
      alpha[ now_alpha - 1 ].popleft()
      res += 1
  now_alpha -= 1
print(res)