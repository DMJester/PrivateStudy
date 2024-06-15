import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/12892/input.txt", "r").readlines()))

N, D = map(int, sys.stdin.readline().strip().split())
PV = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

PV.sort(key = lambda x : x[0])

start = 0
end = 0
res = 0

V_sum = 0

while start < N and end < N:
    P_diff = abs(PV[start][0] - PV[end][0])
    if P_diff >= D:
        V_sum -= PV[start][1]
        start += 1 
    elif P_diff < D:
        V_sum += PV[end][1]
        end += 1
    res = max(res, V_sum)
print(res)