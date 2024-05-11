import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./test_240504/2531/input.txt").readlines()))
    
N, d, k, c = map(int, sys.stdin.readline().strip().split())
sushi_list = []
for i in range(N):
    sushi_list.append(int(sys.stdin.readline().strip()))
res = 0

sushi_combo = []

for idx in range(len(sushi_list)):
    offset = 0
    for i in range(k):
        if idx + i >= (len(sushi_list)):
            sushi_combo.append(sushi_list[offset])
            offset += 1
        else:
            sushi_combo.append(sushi_list[idx+i])
    sushi_combo = set(sushi_combo)
    sushi_cnt = len(sushi_combo)
    if c not in sushi_combo:
        sushi_cnt += 1
    res = max(res, sushi_cnt)
    sushi_combo = []
    
print(res)