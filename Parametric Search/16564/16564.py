import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/16564/input.txt").readlines()))

N, K = map(int, sys.stdin.readline().strip().split())
X_List = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = 0

low = 1
high = 1000000000
while low <= high:
    T = ( low + high ) // 2
    use_sum = 0
    
    for X in X_List:
        if X < T:
            use_sum += T-X
        
    if use_sum <= K:
        low = T + 1
        res = T
    else:
        high = T - 1

print(res)     