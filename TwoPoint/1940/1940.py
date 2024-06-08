import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/1940/input.txt").readlines()))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
materials = list(map(int, sys.stdin.readline().strip().split()))
res = 0

materials.sort()

start = 0
end = N-1
point = 0

while start < end:
    point = materials[start] + materials[end]
    if point == M:
        res += 1
        start += 1
        end -= 1
    elif point < M:
        start += 1
    elif point > M:
        end -= 1
    
print(res)