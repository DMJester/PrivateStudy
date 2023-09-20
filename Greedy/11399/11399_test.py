#https://www.acmicpc.net/problem/11399

import sys

with open("./Greedy/11399/input.txt", 'r') as f:
    N, K = map(int, f.readline().strip().split())
    A = []
    res = 0
    
    for i in range(N):
        val = int(f.readline().strip())
        if val > K:
            continue
        else :
            A.append(val)
    
    A.reverse()
    
    for val in A:
        res += int(K / val)
        K = K % val
    
    print(res)