#https://www.acmicpc.net/problem/2613
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/2613/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
num_bead = list(map(int, sys.stdin.readline().strip().split()))
res_max = 0
res_count = []
res_group = []

low_max = max(num_bead)
high_max = sum(num_bead)
while low_max <= high_max:
    set_max = ( low_max + high_max ) // 2 
    groups = []
    group_cnt = 0
    group_sum = 0
    group_obj_cnt = 0
    
    for idx, num in enumerate(num_bead):
        group_sum += num
        group_obj_cnt += 1
        
        if group_sum > set_max:
            group_sum -= num
            group_obj_cnt -= 1
            groups.append((group_sum, group_obj_cnt))
            group_sum = num
            group_obj_cnt = 1
        
        if idx == len(num_bead)-1:
            groups.append((group_sum, group_obj_cnt))
    
    if len(groups) > M:
        low_max = set_max + 1
    else:
        high_max = set_max - 1
        res_max = set_max
        res_group.clear()
        for g in groups:
            res_group.append(g) 
        
if len(res_group) < M:
    diff = M - len(res_group)
    for rg in res_group:
        if rg[1] >= 2 and diff >= 1:
            spare = rg[1] - 1
            use = 0
            for i in range(spare):
                if diff >= 1:
                    diff -= 1
                    use += 1
                    res_count.append(1)
            if use >= 1:
                res_count.append(rg[1] - use)
        else:
            res_count.append(rg[1])
else:
    for rg in res_group:
        res_count.append(rg[1])
        
print(res_max)
print(*res_count)