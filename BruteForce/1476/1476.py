#https://www.acmicpc.net/problem/1476
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1476/input.txt","r").readlines()))

#E 1 ~ 15
#S 1 ~ 28
#M 1 ~ 19

E, S, M = map(int, sys.stdin.readline().strip().split())
calendar_list = [E, S, M]
ne, ns, nm = 1, 1, 1
res = 1

while(E != ne or S != ns or M != nm) :
    ne = ne % 15 + 1
    ns = ns % 28 + 1
    nm = nm % 19 + 1
    res += 1

print(res)