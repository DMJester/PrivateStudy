#https://www.acmicpc.net/problem/14916
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/14916/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
dp_table = [-1 for _ in range(0, 6)]
dp_table += [100000 for _ in range(N-5)]
dp_table[2] = 1
dp_table[4] = 2
dp_table[5] = 1

for idx in range(6, N+1):
  coin_2 = dp_table[idx-2]+1
  coin_5 = dp_table[idx-5]+1
  
  if(coin_2 >= 1 and coin_5 >= 1):
    dp_table[idx] = min( dp_table[idx-2]+1, dp_table[idx-5]+1 )
  elif coin_2 >=1:
    dp_table[idx] = dp_table[idx-2]+1
  elif coin_5 >=1:
    dp_table[idx] = dp_table[idx-5]+1

print(dp_table[N])