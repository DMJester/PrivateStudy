#https://www.acmicpc.net/problem/2098
#외판원 순회

import sys
from io import StringIO

def dfs(start, visited) :
    if visited == visited_all:
        #print(start, visited, dp[start][visited])
        if W[start][0] != 0:
            dp[start][visited] = W[start][0]
            return W[start][0]
        else:
            dp[start][visited] = INF
            return INF
    
    if dp[start][visited] != 0:
        return dp[start][visited]
    
    min_cost = INF
    
    for next in range(1, N):
        next_visit = (1 << next)
        if visited & next_visit or W[start][next] == 0:
            continue
        min_cost = min(min_cost, dfs(next, visited | next_visit) + W[start][next])
              
    dp[start][visited] = min_cost       
    return dp[start][visited]

sys.stdin = StringIO("".join(open("./DynamicProgramming/2098/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

visited_all = (1 << N)-1

INF = 16000001
dp = [[0] * (1<<N) for _ in range(N)]

print(dfs(0, 1))