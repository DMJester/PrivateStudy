import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/14627/input.txt", "r").readlines()))

S, C = map(int, sys.stdin.readline().strip().split())
MIKU_WEAPONS = [int(sys.stdin.readline().strip()) for _ in range(S)]

max_lenth = max(MIKU_WEAPONS)
res = max_lenth

left = 1
right = max_lenth
while left <= right:
    set_lenth = ( left + right ) // 2
    chicken_cnt = 0
    left_lenth = 0
    
    for w in MIKU_WEAPONS:
        quotient, remain = divmod(w, set_lenth)
        
        if quotient >= 1:
            chicken_cnt += quotient
        left_lenth += remain
    
    if left_lenth == 0:
        left_lenth = (chicken_cnt * set_lenth) - (C * set_lenth)
    
    if chicken_cnt >= C:
        left = set_lenth + 1
        res = left_lenth
    else:
        right = set_lenth - 1

print(res)