#https://www.acmicpc.net/problem/10952

import sys

res = []

while 1:
    A, B = map(int, sys.stdin.readline().strip().split())
    
    if A == 0 and B == 0:
        break;
    
    res.append( A + B )
    
for r in res:
    print(r)