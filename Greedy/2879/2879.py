#https://www.acmicpc.net/problem/2879
#코딩은예쁘게

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/2879/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
wrong_code = list(map(int, sys.stdin.readline().strip().split()))
right_code = list(map(int, sys.stdin.readline().strip().split()))
diff = []
res = 0

for idx in range(N):
  diff.append( wrong_code[idx] - right_code[idx] )

std_value = 0
for now in diff:
  if now > 0:
      if std_value < 0:
        res += now
      else:
        if std_value >= now:
          std_value = now
        else:
          res += now - std_value
  else:
    if std_value > 0:
      res -= now
    else:
      if std_value <= now:
        std_value = now
      else:
        res += std_value - now
  std_value = now

print(res)

'''
4 -1 5 4
'''