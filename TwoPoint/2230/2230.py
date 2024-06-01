import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/2230/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
numbers = [int(sys.stdin.readline().strip()) for i in range(N)]
numbers = sorted(numbers)
res = 2000000001

start = 0
end = 1
while start < N:
    while start <= end and end < N:
        if start != end:
            check = abs(numbers[start] - numbers[end])
            if check < M:
                end += 1
            else:
                res = min(res, check)
                start += 1
        else:
            end += 1
    start += 1
    
print(res)
        
