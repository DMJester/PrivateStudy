#https://www.acmicpc.net/problem/11509
#풍선 맞추기

import sys
from io import StringIO
from bisect import bisect_left

sys.stdin = StringIO("".join(open("./Greedy/11509/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
H = list(map(int, sys.stdin.readline().strip().split()))
res = 0

hb_infos = [[] for _ in range(max(H)+1)]
for idx, height in enumerate(H):
	hb_infos[height].append(idx)
	
now = 0
while now < N:
	target_height = H[now]
	
	if len(hb_infos[target_height]) == 0 or (not now in hb_infos[target_height]):
		now += 1
		continue
	
	last = now
	while target_height:
		lidx = bisect_left(hb_infos[target_height], last)

		if len(hb_infos[target_height]) != 0 and lidx <= len(hb_infos[target_height])-1 and last <= hb_infos[target_height][lidx]:
			last = hb_infos[target_height][lidx]
			hb_infos[target_height].pop(lidx)
			target_height -= 1
		else:
			break
	
	now += 1
	res += 1

print(res)