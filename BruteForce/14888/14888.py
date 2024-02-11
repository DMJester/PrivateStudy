import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/14888/input.txt", "r").readlines()))

def dfs( depth, comb ):
    global min_res
    global max_res
    
    if depth >= N-1:
        comb.append( numbers[depth] )
        
        now = int(comb[0])        
        
        for idx, c in enumerate(comb):
            if c == '+':
                now = now + int(comb[idx+1])
            elif c == '-':
                now = now - int(comb[idx+1])
            elif c == '*':
                now = now * int(comb[idx+1])
            elif c == '//':
                if now <= 0:
                    now = (abs(now) // int(comb[idx+1])) * -1
                else:
                    now = now // int(comb[idx+1])
        
        min_res = min( min_res, now )
        max_res = max( max_res, now )
        comb.pop()
        return
    
    comb.append( numbers[depth] )
    for idx, op in enumerate(ops):
        if ops_used[idx] == False:
            comb.append( op )
            ops_used[idx] = True
            dfs( depth+1, comb )
            comb.pop()
            ops_used[idx] = False
    comb.pop()

N = int(sys.stdin.readline().strip())
numbers = list( sys.stdin.readline().strip().split() )
op_nums = list( map( int, sys.stdin.readline().strip().split() ) )

min_res = 1000000000
max_res = -1000000000

ops = []
ops_used = []

for idx, val in enumerate(op_nums):
    for n in range(val):
        if idx == 0:
            ops.append('+')
        elif idx == 1:
            ops.append('-')
        elif idx == 2:
            ops.append('*')
        elif idx == 3:
            ops.append('//')   

for i in range(len(ops)):
    ops_used.append(False)

dfs(0, [])

print(max_res)
print(min_res)