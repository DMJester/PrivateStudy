#https://www.acmicpc.net/submit/2217
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/2217/input.txt", "r").readlines()))

N = int( sys.stdin.readline().strip() )
k = N
ropes = [ int(sys.stdin.readline().strip()) for _ in range(N) ]
ropes.sort()

res = ropes[-1]

for r in ropes:
    limit = r * k
    if limit >= res:
        res = limit
    k -= 1
       
print(res)     