#https://www.acmicpc.net/problem/1202
#보석 도둑

import sys
import heapq
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/1202/input.txt", "r").readlines()))

N, K = map(int, sys.stdin.readline().strip().split())
jewels = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
pouchs = [int(sys.stdin.readline().strip()) for _ in range(K)]
res = 0

jewels.sort(key=lambda x:x[0])
pouchs.sort(reverse=False)
heap = []

idx = 0
for pouch in pouchs:
		while idx < N and pouch >= jewels[idx][0]:
			heapq.heappush(heap, -jewels[idx][1])
			idx += 1
		if heap:
			res += -heapq.heappop(heap)

print(res)