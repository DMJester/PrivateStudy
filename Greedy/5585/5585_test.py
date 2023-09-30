#https://www.acmicpc.net/problem/5585

import sys

with open("./Greedy/5585/input.txt", 'r') as f:
    N = int(f.readline().strip())
    pay = 1000    
    change = pay - N
    res = 0
    unit = [500, 100, 50, 10, 5, 1]
    
    for u in unit:
        res += int(change / u)    
        change %= u
            
    print(res)