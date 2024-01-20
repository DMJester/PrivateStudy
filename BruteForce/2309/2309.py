#https://www.acmicpc.net/problem/2309
import sys
import itertools
from io import StringIO

sys.stdin = StringIO(''.join(open("./BruteForce/2309/input.txt", "r").readlines()))

height_list = [int(sys.stdin.readline().strip()) for _ in range(9)]
res_list = []

comb_list = list(itertools.combinations(height_list, 7))
for comb in comb_list:
    if sum(comb) == 100:
        res_list = list(comb)
        break
            
res_list.sort()
for i in res_list:
    print(i)