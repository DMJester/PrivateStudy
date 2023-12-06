import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1541/input.txt", "r").readlines()))

equations = sys.stdin.readline().strip()

plus_list = equations.split('-')
minus_list = []
res = 0

for p_eq in plus_list:
    number = p_eq.split('+')
    sum = 0
    for num in number:
        sum += int(num)
    minus_list.append(sum)

for idx, num in enumerate(minus_list):
    if idx == 0:
        res = num
    else:
        res -= num

print(res)