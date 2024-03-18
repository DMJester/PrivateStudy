import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/17135/input.txt", "r").readlines()))

def dfs(depth, start):
    global res
    if depth == max_deploy:
        shot_cnt = [[0 for _ in range(M)] for __ in range(N)]
        shot_check = [[False for _ in range(M)] for __ in range(N)]
        shot_axis = [[-1,-1] for _ in range(M)]
        
        for stage in range(N):                        
            for archer_x, archer in enumerate(deploy):
                if archer == 1:
                    archer_y = N
                    shot_x = -1
                    shot_y = -1
                    prev_dist = 10000
                    
                    for x in range(M):
                        if x < archer_x - D:
                            continue
                        if x > archer_x + D:
                            continue
                        for y in range(N-stage-1, N-stage-1-D, -1):
                            if y < 0:
                                break
                            if board[y][x] == 1 and shot_check[y][x] == False:
                                dist = abs(y + stage - archer_y) + abs(x - archer_x)   
                                if dist <= D and dist < prev_dist:
                                        prev_dist = min(prev_dist, dist)
                                        shot_x = x
                                        shot_y = y
                                else:
                                    break
                    if shot_x >= 0 and shot_y >= 0:
                        shot_axis[archer_x][0] = shot_y
                        shot_axis[archer_x][1] = shot_x
                        
            for y,x in shot_axis:
                if y >= 0 and x >= 0:
                    shot_cnt[y][x] = 1
                    shot_check[y][x] = True
                        
            res = max(res, sum(sum(shot_cnt, [])))
        return
    
    for idx in range(start, M):
        if deploy_loc[idx] == False:
            deploy[idx] = 1
            deploy_loc[idx] = True
            dfs(depth+1, start+1)
            deploy[idx] = 0
            deploy_loc[idx] = False

N, M, D = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
deploy = [0 for _ in range(M)]
deploy_loc = [False for _ in range(M)]
max_deploy = 3
res = 0

dfs(0, 0)

print(res)
