import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./23032/input.txt", "r").readlines()))

N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().strip().split()))
res = 0
 
tl = []
tr = []

prev = 10000 * 2000
for mid in range(1, N):
    left = mid - 1
    right = mid
    ls = 0
    rs = 0
    
    tl.clear()
    tr.clear()
    
    while left >= 0 and right <= N:
        if left >= 0:
            tl.append(W[left])
            ls += W[left]
            left -= 1
            
        if right < N:
            tr.append(W[right])
            rs += W[right]
            right += 1
            
        test = ls + rs
        test = 0
          
        diff = abs(ls - rs)   
        if diff <= prev:
            prev = diff
            res = max(res, (ls+rs))
            
print(res)