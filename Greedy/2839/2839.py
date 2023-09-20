#https://www.acmicpc.net/problem/2839

import sys

N = int(sys.stdin.readline().strip())
res = -1

bag5 = 0
bag3 = 0

if N % 5 == 0:
    bag5 = int(N/5) 
else:
    bag5 = int(N/5)
    while bag5 >= 0:
        check = int((N - ( 5 * bag5 )) % 3)
        if check == 0:
            bag3 = int((N - ( 5 * bag5 )) / 3)
            break;
        else : 
            bag5 -= 1
       
if bag3 != 0 or bag5 != 0: 
    res = bag5 + bag3

print(res)