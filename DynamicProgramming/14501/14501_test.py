#https://www.acmicpc.net/problem/14501

import sys 

with open('./DynamicProgramming/14501/input.txt') as f:
    N = int(f.readline().strip())
    work_list = [tuple(map(int, f.readline().strip().split())) for _ in range(N)]
    dp_table = [0 for _ in range(N+1)]
    
    print(work_list)
    for i in range(N):
        for j in range(i+work_list[i][0], N+1):
            dp_table[j] = max(dp_table[j], dp_table[i] + work_list[i][1])
    
    print(dp_table[-1])