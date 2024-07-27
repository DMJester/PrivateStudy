#https://www.acmicpc.net/problem/16401
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/16401/input.txt", "r").readlines()))

M, N = map(int, sys.stdin.readline().strip().split())
L = list(map(int, sys.stdin.readline().strip().split()))
res = 0

left = 1
right = max(L)
while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for now in L:
        if now >= mid:
            cnt += now // mid
            if cnt >= M:
                break
    
    if cnt >= M:
        res = max(mid, res)
        left = mid + 1
    else:
        right = mid - 1 

print(res)