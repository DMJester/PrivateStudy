import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/16922/input.txt", "r").readlines()))

def dfs(depth, comb):
    global res
    if depth >= N:     
        tmp = 0
        for idx, num in enumerate(comb):
            tmp += numbers[idx] * num
        
        if tmp not in res:
            res.append(tmp)       
            
        return
    
    for idx, num in enumerate(numbers):
        comb[idx] += 1
        t_comb = tuple(comb)
        if t_comb not in number_set:
            number_set.add(t_comb)
            dfs(depth+1, comb)
        comb[idx] -= 1

numbers = [1, 5, 10, 50]
number_set = set()
N = int(sys.stdin.readline().strip())
res = []

dfs(0, [0, 0, 0, 0])
    
print(len(res))

