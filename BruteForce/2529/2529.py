#https://www.acmicpc.net/submit/2529
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/2529/input.txt", "r").readlines()))

def dfs(depth, comb):
    global min_res
    global max_res
    
    if depth == k+1:
        min_res = min(min_res, int(''.join(map(str, comb))))
        max_res = max(max_res, int(''.join(map(str, comb))))
        return
    
    for number in range(10):
        if depth == 0:
            use_numbers[number] = True
            comb.append(number)
            
            dfs(depth+1, comb)
            
            use_numbers[number] = False
            comb.remove(number)
        elif use_numbers[number] == False:
            check_tmp = str(comb[-1]) + ineq_signs[depth-1] + str(number)
            if eval(check_tmp) == True:
                use_numbers[number] = True
                comb.append(number)
                
                dfs(depth+1, comb)
                
                use_numbers[number] = False
                comb.remove(number)

k = int(sys.stdin.readline().strip())
ineq_signs = [ineq for ineq in sys.stdin.readline().strip().split()]

use_numbers = [ False for _ in range(10) ]

max_res = 0
min_res = int('9' * (k+1))

dfs(0, [])

print(str(max_res).zfill(k+1))
print(str(min_res).zfill(k+1))