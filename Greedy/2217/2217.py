#https://www.acmicpc.net/problem/2217

import sys

N = int(sys.stdin.readline().strip())
rope = []
for n in range(N):
    rope.append(int(sys.stdin.readline().strip()))
res = 0
offset = 0
        
rope.sort()

for r in rope:
    tmp = r * (N - offset)
    if tmp > res:
        res = tmp
    offset += 1

print(res)