#https://www.acmicpc.net/problem/1026

import sys

with open("./Greedy/1026/input.txt", 'r') as f:
    N = int(f.readline().strip())
    A = list(map(int, f.readline().strip().split()))
    B = list(map(int, f.readline().strip().split()))
    res = 0
    
    for i in range(N):
        res += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
            
    print(res)