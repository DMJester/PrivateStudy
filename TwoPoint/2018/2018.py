import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/2018/input.txt").readlines()))

N = int(sys.stdin.readline().strip())
numbers = [i for i in range(0, N+1)]
res = 0

sum_number = 0
last_idx = 0

start = 1
end = 1

while start <= N:
    while start <= end:
        if sum_number < N and end != last_idx:
            sum_number += numbers[end]
            last_idx = end
        
        if sum_number == N:
            res += 1
            sum_number -= numbers[start]
            start += 1
        elif sum_number > N:
            sum_number -= numbers[start]
            start += 1
        else:
            end += 1
    
print(res)