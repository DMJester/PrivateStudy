#https://www.acmicpc.net/problem/10162
import sys
from io import StringIO

#sys.stdin = StringIO("".join(open("./Greedy/10162/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())
btn_list = [300, 60, 10]
push_list = [0, 0, 0]
left_sec = T
res = -1

for idx, sec in enumerate(btn_list):
    push = left_sec // sec
    if push > 0:
        left_sec = left_sec % sec
        push_list[idx] += push
        if left_sec == 0:
            res = " ".join(str(x) for x in push_list)
            break

print(res)