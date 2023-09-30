#https://www.acmicpc.net/problem/1700

import sys

N, K = map(int, sys.stdin.readline().strip().split())
device = list(map(int, sys.stdin.readline().strip().split()))
plug = list(0 for i in range(N))
cnt = 0

final_res = 0
    
for stage, now in enumerate(device):
    if now not in plug:
        if cnt < N:
            plug[cnt] = now
            cnt += 1
        else:
            final_res += 1
            later = 0
            later_device = 0
                            
            for idx, si_device in enumerate(plug):    
                if si_device in device[stage:]:                              
                    check = device[stage:].index(si_device)
                    if later < check :
                        later = check
                        later_device = idx
                else :
                    later_device = idx
                    break;
            plug[later_device] = now                 
    else:
        continue
    
print(final_res)