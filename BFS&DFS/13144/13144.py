import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BFS&DFS/13144/input.txt", "r").readlines()))
 
N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
number_use = [False for i in range(100001)]
res = 0

start = 0
end = 0
cnt = 0

while start < N:
    while start <= end and end < N:
        if number_use[numbers[end]] == False:
            number_use[numbers[end]] = True
            end += 1
        else:
            number_use[numbers[start]] = False
            start += 1
print(res)
