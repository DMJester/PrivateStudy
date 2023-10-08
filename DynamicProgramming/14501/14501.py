#https://www.acmicpc.net/problem/14501

import sys 

N = int(sys.stdin.readline().strip())
work_list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp_table = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+work_list[i][0], N+1):
        dp_table[j] = max(dp_table[j], dp_table[i] + work_list[i][1])

print(dp_table[-1])

