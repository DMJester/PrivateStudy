#https://www.acmicpc.net/problem/14225

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/14225/input.txt","r").readlines()))

def dfs(idx, n, comb):
    global res

    if len(comb) == n:
        tmp = sum(comb)
        sum_list.append(tmp)
    
    for i in range(idx, N):
        if number_used[i] == False:
            number_used[i] = True
            comb.append(number_list[i])
            dfs(i, n, comb)
            comb.pop()
            number_used[i] = False

N = int(sys.stdin.readline().strip())
number_list = list(map(int, sys.stdin.readline().strip().split()))
number_used = [False for _ in range(N)]
comb = []
sum_list = []
res = 0

for i in range(1, N+1):            
    dfs(0, i, comb)

sum_list = set(sum_list)

for i in range(1, 2000001):
    if i not in sum_list:
        res = i
        break
    
print(res)