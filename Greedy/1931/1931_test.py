#https://www.acmicpc.net/problem/1931

import sys

with open("./Greedy/1931/input.txt", 'r') as f:
    N = int(f.readline().strip())
    time_list = []
    res = 0
    
    for i in range(N):
        time_list.append(list(map(int, f.readline().strip().split())))
    
    time_list.sort(key=lambda x:(x[1], x[0]))
    last_time = -1
    
    for t in time_list:
        if last_time <= t[0]:
            res += 1
            last_time = t[1]
            
    print(res)