import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./test_240504/1059/input.txt").readlines()))

def dfs(depth, start):
    global res
    global comb
    if depth == 2:
        if n >= comb[0] and n <= comb[1]:
            res += 1
        return
    
    for i in range(start, len(num_list)):
        if num_use[i] == False:
            num_use[i] = True
            comb.append(num_list[i])
            
            dfs(depth+1, i)
        
            num_use[i] = False
            comb.pop()
    
L = int(sys.stdin.readline().strip())
S = sorted(list(map(int, sys.stdin.readline().strip().split())))
n = int(sys.stdin.readline().strip())

low_idx = 0
high_idx = len(S)-1
check = False

num_list = []
comb = []

res = 0

for idx, s in enumerate(S):
    if n == s:
        break
    if n < s:
        low_idx = idx - 1
        high_idx = idx
        check = True
        break
    
low_number = S[low_idx] + 1
if low_idx == -1: low_number = 1
high_number = S[high_idx]
    
for i in range(low_number, high_number):
    num_list.append(i)

num_use = [False for _ in range(len(num_list))]

if check:
    dfs(0, 0)
    
print(res)