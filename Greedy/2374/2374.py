#https://www.acmicpc.net/problem/2374
#같은 수로 만들기

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/2374/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
A_List = []
res = 0

prev_num = -1
for idx in range(N):
  now_num = int(sys.stdin.readline().strip())
  if now_num != prev_num:
    A_List.append(now_num)
  prev_num = now_num
  
max_num = max(A_List)
min_num = min(A_List)
while min_num != max_num:
  min_idx = A_List.index(min_num)
  neighbor = []
  
  len_list = len(A_List)
  if min_idx - 1 >= 0:
    neighbor.append(A_List[min_idx-1])
  if min_idx + 1 < len_list:
    neighbor.append(A_List[min_idx+1])
  
  A_List.pop(min_idx)
  res += min(neighbor) - min_num
  min_num = min(A_List)
print(res)