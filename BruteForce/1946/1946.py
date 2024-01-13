import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1946/input.txt", "r").readlines()))

T = int(sys.stdin.readline().strip())

for c in range(T):   
    res = 0
    N = int(sys.stdin.readline().strip())
    applicants = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    applicants.sort()
    grade_cut = applicants[0][1]
    for idx, data in enumerate(applicants):
        if data[0] == 1 or data[1] == 1:
            res += 1
        elif idx != N-1:
            if data[1] < grade_cut:
                res += 1
        grade_cut = min(grade_cut, data[1])
    print( res )