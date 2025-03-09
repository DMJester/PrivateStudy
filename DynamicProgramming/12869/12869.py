#https://www.acmicpc.net/problem/12869
#뮤리
import sys
from io import StringIO
import itertools

def dfs(hp0, hp1, hp2) :
    hp0 = max(0, hp0)
    hp1 = max(0, hp1)
    hp2 = max(0, hp2)
    
    if hp0 <= 0 and hp1 <= 0 and hp2 <= 0:
        return 0
    
    if dp[hp0][hp1][hp2] != -1:
        return dp[hp0][hp1][hp2]
      
    hit_cnt = MAX_HIT
    for att in attack_type:
      hit_cnt = min(hit_cnt, 1 + dfs(hp0 - att[0], hp1 - att[1], hp2 - att[2]))

    dp[hp0][hp1][hp2] = hit_cnt
    return dp[hp0][hp1][hp2]

sys.stdin = StringIO("".join(open("./DynamicProgramming/12869/input.txt").readlines()))

MAX_HIT = 61
N = int(sys.stdin.readline().strip())
SCV = list(map(int, sys.stdin.readline().strip().split()))
dp = [[[-1 for _ in range(MAX_HIT)] for __ in range(MAX_HIT)] for ___ in range(MAX_HIT)]
damages = [9, 3, 1]
attack_type = list(itertools.permutations(damages))

if N < 3:
    for i in range(3-N):
        SCV.append(0)

print(dfs(SCV[0], SCV[1], SCV[2]))