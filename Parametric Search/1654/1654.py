#https://www.acmicpc.net/problem/1654
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/1654/input.txt", "r").readlines()))

K, N = map(int, sys.stdin.readline().strip().split())
Lan_cables = [int(sys.stdin.readline().strip()) for _ in range(K)]
res = 0

Lan_cables.sort()

low = 1
high = Lan_cables[-1]
while low <= high:
    cable_len = (low + high) // 2
    cable_cnt = 0

    for have_cable in Lan_cables:
        if have_cable >= cable_len:
            cable_cnt += have_cable // cable_len

    if cable_cnt >= N:
        res = max(res, cable_len)
        low = cable_len + 1
    else:
        high = cable_len - 1
print(res)