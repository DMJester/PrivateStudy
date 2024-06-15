import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/2559/input.txt", "r").readlines()))

N, K = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))

temperature_sum = 0

start = 0
end = 0
res = -sys.maxsize

while start <= N-K:
    day = (end - start)
    
    if day == K:
        res = max(res, temperature_sum)
        temperature_sum -= numbers[start]
        start += 1
    elif day < K:
        temperature_sum += numbers[end]
        end += 1
    elif day > K:
        temperature_sum -= numbers[start]
        start += 1
print(res)