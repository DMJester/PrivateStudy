#https://www.acmicpc.net/problem/1065
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1065/input.txt").readlines()))

N = sys.stdin.readline().strip()
use = [False for _ in range(len(N))]
comb = []
res = 0

def dfs(depth, start):
    if depth == len(N):
        print()
        return

    for i in range(start, len(N)):
        if use[i] == False:
            use[i] = True
            dfs(depth+1, i+1)
            use[i] = False
    
dfs(0, 0)
print(res)
