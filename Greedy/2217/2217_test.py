#https://www.acmicpc.net/problem/2217

import sys

with open("./Greedy/2217/input.txt", 'r') as f:
    N = int(f.readline().strip())
    rope = []
    for n in range(N):
        rope.append(int(f.readline().strip()))
    res = 0
    offset = 0
            
    rope.sort()

    for r in rope:
        tmp = r * (N - offset)
        if tmp > res:
            res = tmp
        offset += 1
    
    print(res)