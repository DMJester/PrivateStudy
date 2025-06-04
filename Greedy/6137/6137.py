#https://www.acmicpc.net/problem/6137
#문자열생성

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/6137/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
S = [sys.stdin.readline().strip() for _ in range(N)]
T = []

nl = 0
nr = len(S) - 1
nl_cnt = 0
while nl <= nr:
  if S[nl] < S[nr]:
    T.append(S[nl])
    nl += 1
  elif S[nl] > S[nr]:
    T.append(S[nr])
    nr -= 1
  else:
    nnl = nl + 1
    nnr = nr - 1
    isAppend = False
    while nnl <= nnr:
      if S[nnl] < S[nnr]:
          T.append(S[nl])
          nl += 1
          isAppend = True
          break
      elif S[nnl] > S[nnr]:
          T.append(S[nr])
          nr -= 1
          isAppend = True
          break
      else:
          nnl += 1
          nnr -= 1
    if not isAppend:
      T.append(S[nl])
      nl += 1
      
  if ((len(T) % 80) - nl_cnt) == 0:
    T.append("\n")
    nl_cnt += 1

print("".join(T))