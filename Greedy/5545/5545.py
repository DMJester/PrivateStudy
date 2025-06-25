#https://www.acmicpc.net/problem/5545
#최고의피자

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/5545/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
dough_price, topping_price = map(int, sys.stdin.readline().strip().split())
dough_cal = int(sys.stdin.readline())
topping_cals = [int(sys.stdin.readline()) for _ in range(N)]

topping_cals.sort(reverse=True)
topping_cals.insert(0, 0)

total_cal = dough_cal
res = 0
for idx, cal in enumerate(topping_cals):
  total_price = dough_price + (topping_price*idx)
  total_cal += cal
  now_cal_cost = total_cal // total_price
  
  if now_cal_cost > res:
    res = now_cal_cost
  else:
    break
  
print(res)