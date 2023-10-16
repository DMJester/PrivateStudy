#https://www.acmicpc.net/problem/17396

import sys
import heapq

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    res[0] = 0
    
    while q:
        now, dist = heapq.heappop(q)
        
        if detect_list[now] == 1 and now < N-1:
            continue
        if res[now] < dist:
            continue
        
        for idx, data in  enumerate(graph[now]):
            cost = dist + data[1]
            if cost < res[data[0]]:
                res[data[0]] = cost
                heapq.heappush(q, data)
                

with open("./Dijkstra/17396/input.txt", 'r') as f:
    N, M = map(int, f.readline().strip().split())
    detect_list = list(map(int, f.readline().strip().split()))
    graph = [[]for _ in range(N)]
    res = [float('inf')] * (N)
    
    for _ in range(M):
        sp, ep, cost = map(int, f.readline().strip().split())
        graph[sp].append((ep, cost))
        graph[ep].append((sp, cost))
            
    dijkstra() 
    
    if max(res) == float('inf'):
        print(-1)
    else :
        print(max(res))