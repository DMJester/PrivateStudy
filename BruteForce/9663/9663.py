import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/9663/input.txt", "r").readlines()))

def check_pos(row, col):
    if row >= 1:
        now_row = row
        now_col = col
        
        #대각선 체크
        for i in range(row):
            prev_row = i
            prev_col = queen[i]
            if abs(prev_row - now_row) == abs(prev_col - now_col):
                return False
    return True

def dfs(comb, idx):
    global res
    if idx >= N:
        res += 1
        #print(comb)
        return

    for x in range(N):
        if x not in queen:
            if check_pos(idx, x):
                queen.append(x)
                dfs( queen, idx+1 )
                queen.pop()

N = int(sys.stdin.readline().strip())
queen = []
res = 0

dfs([], 0)
print(res)