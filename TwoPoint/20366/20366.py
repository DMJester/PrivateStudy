import sys
from io import StringIO
from itertools import combinations

sys.stdin = StringIO("".join(open("./TwoPoint/20366/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
snowballs = list(map(int, sys.stdin.readline().strip().split()))
idx_list = [i for i in range(N)]
res = 1000000001
    
sum_list = [list([snowballs[i[0]]+snowballs[i[1]],(i)]) for i in combinations(idx_list, 2)]

sum_list = sorted(sum_list, key = lambda x : x[0])
sum_list_len = len(sum_list)

start = 0
end = 1
diff = 0

while end < sum_list_len:
    if sum_list[start][1][0] != sum_list[end][1][0] and sum_list[start][1][1] != sum_list[end][1][1] and sum_list[start][1][1] != sum_list[end][1][0] and sum_list[start][1][0] != sum_list[end][1][1]:
        diff = abs(sum_list[start][0] - sum_list[end][0])
        res = min(res, diff)
        start += 1
        end += 1
    else:
        start += 1
        end += 1
    
print(res)