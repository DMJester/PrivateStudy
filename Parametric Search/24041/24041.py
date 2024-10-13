#https://www.acmicpc.net/problem/24041
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/24041/input.txt", "r").readlines()))

def cal_sa(S, L, x):
    return S * max(1, x - L)

N, G, K = map(int, sys.stdin.readline().strip().split())
main_ingredient = []
side_ingredient = []
res = 0

for i in range(N):
    S, L, O = map(int, sys.stdin.readline().strip().split())
    
    if O == 0:
        main_ingredient.append((S, L))
    else:
        side_ingredient.append((S, L))
        
min_day = 1
max_day = (10**9) * (10**9)
while min_day <= max_day:
    check_day = ( min_day + max_day ) // 2
    Staphylococcus_aureus = 0
    remove_cnt = 0
    useless_list = []
    
    for main in main_ingredient:
        Staphylococcus_aureus += cal_sa(main[0], main[1], check_day)
    
    for side in side_ingredient:
        useless_list.append(cal_sa(side[0], side[1], check_day))
    
    useless_list.sort(reverse=True)
    
    for u in useless_list:
        if remove_cnt >= K:
            Staphylococcus_aureus += u    
        else:
            remove_cnt += 1
    
    if Staphylococcus_aureus <= G:
        min_day = check_day + 1
        res = check_day
    else:
        max_day = check_day - 1

print(res)
        
    
    
