#https://www.acmicpc.net/problem/1083
#소트

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/1083/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
S = int(sys.stdin.readline().strip())

now = 0
left = S
while left >= 1 and now < N:
  max_num = max(nums[now:now+left+1])
  max_idx = nums.index(max_num)
  
  if max_idx != now:
    nums.pop(max_idx)
    nums.insert(now, max_num)
    left -= max_idx - now
    
  now += 1
for n in nums:
  print(n, end=" ")