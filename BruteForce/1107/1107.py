#https://www.acmicpc.net/problem/1107
import sys
from io import StringIO

#sys.stdin = StringIO("".join(open("./BruteForce/1107/input.txt", "r").readlines()))

def check_channel(depth):
    global res, channel

    if depth >= max_depth+1:
        return
    
    for n in active_btn:
        channel.append(n)
        depth += 1
        res = min(res, depth + abs(int(''.join(str(x) for x in channel)) - N))
        check_channel(depth)
        channel.pop()
        depth -= 1    

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
broken_btn = list(map(int, sys.stdin.readline().strip().split()))
default_btn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
active_btn = set(default_btn) - set(broken_btn)
now_channel = 100
channel = []
res = abs(now_channel - N)
max_depth = len(str(N))

check_channel(0)

print(res)