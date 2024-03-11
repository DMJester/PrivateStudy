#https://www.acmicpc.net/problem/14889
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/14889/input.txt").readlines()))

def dfs(depth, start):
    global res
    if depth == team_number:
        team_1 = 0
        team_2 = 0
        
        for i in range(N):
            for j in range(N):
                if match[i] and match[j]:
                    team_1 += status_table[i][j]
                elif not match[i] and not match[j]:
                    team_2 += status_table[i][j]
        res = min(res, abs(team_1 - team_2))
        return

    for i in range(start, N):
        if not match[i]:
            match[i] = True
            dfs(depth+1, i+1)
            match[i] = False

N = int(sys.stdin.readline().strip())
team_number = N // 2
status_table = [[int(x) for x in sys.stdin.readline().strip().split()] for _ in range(N)]
match = [False for _ in range(N)]
res = 40001

dfs(0, 0)
print(res)
