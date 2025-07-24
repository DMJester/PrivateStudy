#https://www.acmicpc.net/problem/9576
#책 나눠주기

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/9576/input.txt", "r").readlines()))

case_cnt = int(sys.stdin.readline().strip())

for i in range(case_cnt):
  book_cnt, people_cnt = map(int, sys.stdin.readline().strip().split())
  request_ranges = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(people_cnt)]
  request_ranges.sort(key=lambda x: x[1])
  books = [False] * (book_cnt+1)
  res = 0
  
  for st, ed in request_ranges:
    for now in range(st, ed+1):
      if not books[now]:
        books[now] = True
        res += 1
        break
  print(res)