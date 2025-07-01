#https://www.acmicpc.net/problem/1132
#합

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Greedy/1132/input.txt", "r").readlines()))

def AlpToNum( alp_str, alp_dict ):
  return int("".join(str(alp_dict[s]) for s in alp_str))

N = int(sys.stdin.readline())
alp_strs = [[c for c in sys.stdin.readline().strip()] for __ in range(N)]
alphabets = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0 }
first_alphabet = set()
res = 0

for alp_str in alp_strs:
  offset = len(alp_str)
  for idx, alp in enumerate(alp_str):
    if idx == 0:
      first_alphabet.add(alp)
    alphabets[alp] += (10 ** offset)
    offset -= 1

sorted_alphabets = sorted(alphabets.items(), key=lambda x: x[1], reverse=False)

set_value = 1
set_zero = False
for key, val in sorted_alphabets:
  if val != 0:
    if key in first_alphabet:
      alphabets[key] = set_value
      set_value += 1
    else:
      if not set_zero:
        alphabets[key] = 0
        set_zero = True
      else:
        alphabets[key] = set_value
        set_value += 1

for alp_str in alp_strs:
  res += AlpToNum(alp_str, alphabets)

print(res)