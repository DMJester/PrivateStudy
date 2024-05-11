import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./test_240504/15721/input.txt").readlines()))

def check_pupa():
    global now_player
    
    if pu_pa_cnt[target_number] == T:
        return True
    else:
        now_player += 1
        if now_player == A:
            now_player = 0
        return False

A = int(sys.stdin.readline().strip())
T = int(sys.stdin.readline().strip())
target_number = int(sys.stdin.readline().strip())

now_player = 0
pu_pa_cnt = [0, 0]
toggle = True
round = 0

escape = False
while escape == False:
    for prefix in range(4):
        if toggle:
            pu_pa_cnt[0] += 1
            if check_pupa():
                escape = True
                break
        else :
            pu_pa_cnt[1] += 1
            if check_pupa():
                escape = True
                break
        toggle = not toggle
    if escape:
        break
        
    for suffix_1 in range(2 + round):
        pu_pa_cnt[0] += 1
        if check_pupa():
            escape = True
            break
    if escape:
        break
    
    for suffix_2 in range(2 + round):
        pu_pa_cnt[1] += 1
        if check_pupa():
            escape = True
            break     
    if escape:
        break
    
    round += 1

res = now_player
print(res)