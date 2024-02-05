#https://www.acmicpc.net/problem/1339
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1339/input.txt","r").readlines()))

N = int(sys.stdin.readline())
words = [[c for c in sys.stdin.readline().strip()] for _ in range(N)]
digit_max_list = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

char_value = {}
offset = 9
res = 0

for word in words:
    word_len = len(word)
    for idx, c in enumerate(word):
        if c in char_value:
            tmp = char_value[c]
        else:
            tmp = 0
        char_value[c] = tmp + digit_max_list[word_len-1 - idx]

sorted_char_value = sorted(char_value.items(), key = lambda item: item[1], reverse = True)

for k, v in sorted_char_value:
    res += v * offset
    offset -= 1

print(res)