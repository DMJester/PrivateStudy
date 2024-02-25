import sys
import itertools
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/16922/input.txt", "r").readlines()))

numbers = [1, 5, 10, 50]

N = int(sys.stdin.readline().strip())
comb = itertools.combinations_with_replacement(numbers, N)
res = []

for c in comb:
    tmp = sum(c)
    if tmp not in res:
        res.append(tmp)
        
print(len(res))