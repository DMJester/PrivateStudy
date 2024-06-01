import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/20922/input.txt", "r").readlines()))

N, K = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
res = 0

number_count = [0] * 100001

start = 0
end = 0
now_len = 0

while start <= end:
    while start <= end and end < N:
        if number_count[numbers[end]] < K:
            number_count[numbers[end]] += 1
            now_len = end - start + 1
            res = max(res, now_len)
            end += 1
        else:
            number_count[numbers[start]] -= 1
            start += 1
    start += 1
    
print(res)
        