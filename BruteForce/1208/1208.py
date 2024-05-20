#https://www.acmicpc.net/problem/1208

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1208/input.txt","r").readlines()))

def dfs(idx, comb):
    global res

    if len(comb) >= 1 and sum(comb) == S:
        res += 1
    
    for i in range(idx, N):
        if number_used[i] == False:
            number_used[i] = True
            comb.append(number_list[i])
            dfs(i, comb)
            comb.pop()
            number_used[i] = False

N, S = map(int, sys.stdin.readline().strip().split())
number_list = list(map(int, sys.stdin.readline().strip().split()))
number_used = [False for _ in range(N)]
comb = []
res = 0
            
dfs(0, comb)
    
print(res)