import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/20366/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
snowballs = list(map(int, sys.stdin.readline().strip().split()))
snowballs = sorted(snowballs)

start = 0
end = 1