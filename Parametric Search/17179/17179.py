#https://www.acmicpc.net/problem/17179
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/17179/input.txt", "r").readlines()))

def slice_pieces(Ms):
    pieces = []
    prev_loc = 0
    
    for i in range(M+1):
        if i < M:
            slice = Ms[i] - prev_loc
            prev_loc = Ms[i]
        else:
            slice = L - Ms[i-1]
        
        pieces.append(slice)
    
    return pieces

N, M, L = map(int, sys.stdin.readline().strip().split())
Ms = [int(sys.stdin.readline().strip()) for _ in range(M)]
Ns = [int(sys.stdin.readline().strip()) for _ in range(N)]
pieces = []
res = [0]*N

pieces = slice_pieces(Ms)

for i in range(N):
    low = 1
    high = L
    while low <= high:
        small_piece = ( low + high ) // 2
        cut_cnt = 0
        prev_piece = 0
        slice = 0
        
        for p in pieces:
            slice = p + prev_piece
            
            if slice >= small_piece:
                cut_cnt += 1
                prev_piece = 0 
            else:
                prev_piece = slice
        
        if cut_cnt > Ns[i]:
            low = small_piece + 1
            res[i] = small_piece
        else:
            high = small_piece - 1
            
for r in res:
    print(r)