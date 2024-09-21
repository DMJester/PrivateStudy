import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/27932/input.txt").readlines()))

n, k = map(int, sys.stdin.readline().strip().split())
peoples = list(map(int, sys.stdin.readline().strip().split()))
height_diff = []
res = 0

if n == 1:
    height_diff.append( (0, 0) )
else:
    height_diff.append( ( 0, abs(peoples[0] - peoples[1]) ) )
    for i in range(1,n-1):
        height_diff.append( ( abs(peoples[i] - peoples[i-1]), abs(peoples[i] - peoples[i+1]) ) )
    height_diff.append( ( abs(peoples[n-1] - peoples[n-2]), 0 ) )

low = 0
high = 10**9
while low <= high:
    H = ( low + high ) // 2
    exhausted_cnt = 0
    
    idx = 0
    while idx <= n-1:
        for i, h in enumerate(height_diff[idx]):
            if h > H:
                if i == 0:
                    exhausted_cnt += 1
                else :
                    exhausted_cnt += 2
                    idx += 1
                break
        idx += 1
    
    if exhausted_cnt > k:
        low = H + 1
    else:
        high = H - 1
        res = H
    
print(res)