#https://www.acmicpc.net/problem/1715
#카드 정렬하기

import sys
from io import StringIO

import heapq

sys.stdin = StringIO("".join(open("./1715/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
card_packs = [int(sys.stdin.readline().strip()) for _ in range(N)]
heapq.heapify(card_packs)
res = 0

while card_packs:
  if len(card_packs) >= 2:
    number1 = heapq.heappop(card_packs)
    number2 = heapq.heappop(card_packs)

    sum_number = number1 + number2
    heapq.heappush(card_packs, sum_number)
    res += sum_number
  else:
    break

print(res)