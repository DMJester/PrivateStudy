#https://www.acmicpc.net/problem/17396

import sys
import heapq

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    res[0] = 0
    
    while q:
        now, dist = heapq.heappop(q)
        
        if res[now] < dist:
            continue
        
        for idx, data in  enumerate(graph[now]):
            cost = dist + data[1]
            if cost < res[data[0]] and detect_list[data[0]] == 0:
                res[data[0]] = cost
                heapq.heappush(q, (data[0], cost))
                

with open("./Dijkstra/17396/input.txt", 'r') as f:
    N, M = map(int, f.readline().strip().split())
    detect_list = list(map(int, f.readline().strip().split()))
    detect_list[-1] = 0
    graph = [[]for _ in range(N)]
    res = [float('inf') for _ in range(N)]
    
    for _ in range(M):
        sp, ep, dist = map(int, f.readline().strip().split())
        graph[sp].append((ep, dist))
        graph[ep].append((sp, dist))
            
    dijkstra() 
    
    if res[-1] == float('inf'):
        print(-1)
    else :
        print(res[-1])