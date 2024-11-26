import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/1106/input.txt").readlines()))

C, N = map(int, sys.stdin.readline().strip().split())
cities = [list(map(int, sys.stdin.readline().strip().split())) for __ in range(N)]
res = 0
                    
dp_table = [100001 for i in range(C+100)]
dp_table[0] = 0
for cost, customer in cities:
    for customer_cnt in range(1, C+100):
        if customer <= customer_cnt:
            dp_table[customer_cnt] = min(dp_table[customer_cnt], dp_table[customer_cnt-customer]+cost)

print(min(dp_table[C:]))