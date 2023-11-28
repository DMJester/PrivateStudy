#https://www.acmicpc.net/problem/1182
import sys
from collections import deque

def dfs(comb, idx):
    global res
    
    if len(comb) >= 1 and sum(comb) == S:
        res += 1

    for i in range(idx, N):
        if number_used[i] == False:
            number_used[i] = True
            comb.append(number_list[i])
            dfs(comb, i)
            comb.pop()
            number_used[i] = False

N, S = map(int, sys.stdin.readline().strip().split())
number_list = list(map(int, sys.stdin.readline().strip().split()))
number_used = [False] * N
comb = []
res = 0

dfs(comb, 0)

print(res)
