import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BFS&DFS/13144/input.txt", "r").readlines()))
 
N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
number_use = [False for i in range(100002)]
res = 0

for start in range(N):
    now = start
    while now < N:
        if number_use[numbers[now]] == False:
            number_use[numbers[now]] = True
            now += 1
            res += 1
        else:
            break
    for idx in range(start, now):
        number_use[numbers[idx]] = False

print(res)