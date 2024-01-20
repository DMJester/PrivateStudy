#https://www.acmicpc.net/submit/1748
import sys
from io import StringIO

sys.stdin = StringIO(''.join(open("./BruteForce/1748/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
res = 0

digit_count_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_max_list = [9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000]

n_len = len(str(N))
left = N

for r in range(n_len-1):
    res += digit_max_list[r] * digit_count_list[r]
    left = left - digit_max_list[r]
res += left * digit_count_list[n_len-1]

print(res)