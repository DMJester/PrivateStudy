import sys
from io import StringIO

#홀수 -1
#짝수 /2

sys.stdin = StringIO("".join(open("./naver_ran_test/input.txt", "r").readlines()))

def solution(S):
  cnt = 0
  V = int(S, 2)
  
  while (V):
    cnt += 1 + (V & 1)
    V >>= 1
  return cnt - 1

S = sys.stdin.readline().strip()
S = '1' * 400000

print(solution(S))