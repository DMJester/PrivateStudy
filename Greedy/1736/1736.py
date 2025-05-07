#https://www.acmicpc.net/problem/1736
#쓰레기 치우기

import sys
from collections import deque
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/1736/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
garbage = []
tarbage = []
res = 1

Y = 0
X = 1

for y_idx, y_data in enumerate(board):
	for x_idx, x_data in enumerate(y_data):
		if x_data == 1:
			garbage.append((y_idx, x_idx))
  
if not garbage:
  print(0)
else:
	garbage = deque(garbage)
	prev = garbage.popleft()
	while garbage:
		now = garbage.popleft()
		if prev[Y] > now[Y] or prev[X] > now[X]:
			tarbage.append(now)
		elif prev[Y] <= now[Y] and prev[X] <= now[X]:
			prev = now
   
		if len(garbage) == 0 and len(tarbage) >= 1:
			for t in tarbage:
				garbage.append(t)
			tarbage.clear()
			prev = garbage.popleft()
			res += 1
		
	print(res)