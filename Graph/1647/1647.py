#https://www.acmicpc.net/problem/1647

import sys 

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(sp, ep):
    sp = find_parent(sp)
    ep = find_parent(ep)
    
    if sp < ep:
        parent[ep] = sp
    else :
        parent[sp] = ep


N, M = map(int, sys.stdin.readline().strip().split())
parent = [i for i in range(N+1)]
edge_list = []
result = []

for i in range(M):
    sp, ep, cost = map(int, sys.stdin.readline().strip().split())
    edge_list.append((sp, ep, cost))

edge_list.sort(key=lambda x:x[2])

for edge in edge_list:
    sp, ep, cost = edge
    
    if find_parent(sp) != find_parent(ep):
        union_parent(sp, ep)
        result.append(cost)
        
print(sum(result[:-1]))