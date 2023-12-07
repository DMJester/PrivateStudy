#https://www.acmicpc.net/problem/1744
import sys
from io import StringIO

#sys.stdin = StringIO("".join(open("./BruteForce/1744/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
num_list = []
res = 0

for i in range(N):
    num_list.append(int(sys.stdin.readline().strip()))

num_list.sort()

negative_num = []
positive_num = []
left_num = []

for num in num_list:
    if num <= 0:
        negative_num.append(num)
    if num > 1:
        positive_num.append(num)
    if num == 1:
        left_num.append(num)

positive_num.sort(reverse=True)
for a, b in zip(positive_num[0::2], positive_num[1::2]):
    positive_num.remove(a)
    positive_num.remove(b)
    res += a * b
for a, b in zip(negative_num[0::2], negative_num[1::2]):
    negative_num.remove(a)
    negative_num.remove(b)
    res += a * b

left_num += positive_num + negative_num
for num in left_num:
    res += num
    
print(res)