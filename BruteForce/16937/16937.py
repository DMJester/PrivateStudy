#https://www.acmicpc.net/problem/16937

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/16937/input.txt","r").readlines()))

def dfs(depth, comb):
    global res
    
    if depth == 2:
        for direction in range(2):
            size = 0
            left_h = H
            left_w = W
            if direction == 0:
                for y, x in comb:
                    if y <= left_h and x <= left_w:
                        size += y * x
                        left_w -= x
                    else:
                        size = 0
                        break
            if direction == 1:
                for y, x in comb:
                    if y <= left_h and x <= left_w:
                        size += y * x
                        left_h -= y
                    else:
                        size = 0
                        break
            res = max(res, size)
        return
    
    for idx, sticker in enumerate(stickers):
        if stickers_used[idx] == False:
            for rotate in range(2):
                if rotate == 0:
                    x = sticker[1]
                    y = sticker[0]
                if rotate == 1:
                    x = sticker[0]
                    y = sticker[1]
                stickers_used[idx] = True
                comb.append((y, x))
                dfs(depth+1, comb)
                stickers_used[idx] = False
                comb.pop()

H, W = map(int, sys.stdin.readline().strip().split())
N = int(sys.stdin.readline().strip())
stickers = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
stickers_used = [False for _ in range(N)]
res = 0

dfs(0, [])

print(res)