import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1977/input.txt", "r").readlines()))

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
square_number = []

res_sum = 0
res_list = []

for n in range(101):
    square_number.append(n * n)

for i in range(M,N+1):
    if i in square_number:
        res_sum += i
        res_list.append(i)

if len(res_list) >= 1:
    print(res_sum)
    print(res_list[0])
else :
    print(-1)