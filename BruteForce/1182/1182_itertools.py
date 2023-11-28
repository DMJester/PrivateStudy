#https://www.acmicpc.net/problem/1182
import sys
import itertools

N, S = map(int, sys.stdin.readline().strip().split())
number_list = list(map(int, sys.stdin.readline().strip().split()))
cal = 0
res = 0

for i in range(1, N+1):
    comb_list = list(itertools.combinations(number_list, i))
    for comb in comb_list:
        if sum(comb) == S:
            res += 1
print(res)