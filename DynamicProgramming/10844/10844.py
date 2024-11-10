#https://www.acmicpc.net/problem/10844
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./DynamicProgramming/10844/input.txt", "r").readlines()))

digit_num = int(sys.stdin.readline().strip())
dp_table = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0 for _ in range(10)] for __ in range(digit_num-1)]

for y in range(1, digit_num):
    for x in range(10):
        if x == 0:
            dp_table[y][x] = dp_table[y-1][x+1] 
        elif x >= 1 and x <= 8:
            dp_table[y][x] = dp_table[y-1][x-1] + dp_table[y-1][x+1] 
        elif x == 9:
            dp_table[y][x] = dp_table[y-1][x-1]
            
print(sum(dp_table[-1]) % 1000000000)

'''
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 2, 2, 2, 2, 2, 2, 2, 1] = 17
[1, 3, 3, 4, 4, 4, 4, 4, 3, 2] = 32
[3, 4, 7, 7, 8, 8, 8, 7, 6, 3] = 61
'''