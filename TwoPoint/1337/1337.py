import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/1337/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = 4

numbers.sort()

start = 0
end = 1

cnt = 1

while end < N:
    diff = numbers[end] - numbers[start]
    if diff == 1:
        cnt += 1
    elif diff > 1:
        if cnt + diff <= 5:
            cnt += 1
        else:
            cnt = 1
            
    res = min( res, (5-(cnt)) )
    start += 1
    end += 1
    
    if cnt == 5:
        cnt = 0
        res = 0
        break

print(res)