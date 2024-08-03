import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2512/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
req_budget = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
res = 0

req_budget.sort()
max_budget = req_budget[-1]

low = 1
high = M
while low <= high:
    res_budget = (low + high) // 2
    allocation_cnt = 0
    allocation_budget = M
    
    for i in range(N):
        if allocation_budget >= res_budget and max_budget >= res_budget:
            if req_budget[i] <= res_budget:
                allocation_budget -= req_budget[i]
            elif req_budget[i] > res_budget:
                allocation_budget -= res_budget
            allocation_cnt += 1
        else:
            break
    
    if allocation_cnt >= N and allocation_budget >= 0:
        res = max(res, res_budget)
        low = res_budget + 1
    else:
        high = res_budget - 1

print(res)