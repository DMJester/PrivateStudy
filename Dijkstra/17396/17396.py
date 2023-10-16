#https://www.acmicpc.net/problem/17396

import sys
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    res[start] = 0
    
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
                


N, M = map(int, sys.stdin.readline().strip().split())
detect_list = list(map(int, sys.stdin.readline().strip().split()))
graph = [[]for _ in range(N)]
res = [float('inf')] * (N)

for _ in range(M):
    sp, ep, cost = map(int, sys.stdin.readline().strip().split())
    graph[sp].append((ep, cost))
    graph[ep].append((sp, cost))
        
dijkstra(0) 

if max(res) == float('inf'):
    print(-1)
else :
    print(max(res))