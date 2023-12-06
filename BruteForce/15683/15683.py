#https://www.acmicpc.net/problem/15683
import sys
from io import StringIO

#sys.stdin = StringIO("".join(open("./BruteForce/15683/input.txt").readlines()))

U = 0
D = 1
L = 2
R = 3

def cctv_check(comb, idx):
    global res
    global cctv_vector
    
    if idx >= len(coordinate_cctv):
        room_tmp = [row[:] for row in room]
        
        for i in range(len(comb)):
            direction = comb[i]
            model_num, x, y = coordinate_cctv[i]
            mu = y
            md = y
            ml = x
            mr = x
            while 1:
                mu += cctv_vector[model_num][direction][U]
                md += cctv_vector[model_num][direction][D]
                ml += cctv_vector[model_num][direction][L]
                mr += cctv_vector[model_num][direction][R]
                
                #상
                if mu >= 0 and mu <= N-1:
                    if mu == y:
                        mu = -100
                    else:
                        if room_tmp[mu][x] == 6:
                            mu = -100
                        elif room_tmp[mu][x] == 0:
                            room_tmp[mu][x] = '#'
                else:
                    mu = -100
                
                #하
                if md >= 0 and md <= N-1:
                    if md == y:
                        md = -100
                    else:
                        if room_tmp[md][x] == 6:
                            md = -100
                        elif room_tmp[md][x] == 0:
                            room_tmp[md][x] = '#'
                else:
                    md = -100
                    
                #좌
                if ml >= 0 and ml <= M-1:
                    if ml == x:
                        ml = -100
                    else:
                        if room_tmp[y][ml] == 6:
                            ml = -100
                        elif room_tmp[y][ml] == 0:
                            room_tmp[y][ml] = '#'
                else:
                    ml = -100
                    
                #우
                if mr >= 0 and mr <= M-1:
                    if mr == x:
                        mr = -100
                    else:
                        if room_tmp[y][mr] == 6:
                            mr = -100
                        elif room_tmp[y][mr] == 0:
                            room_tmp[y][mr] = '#' 
                else:
                    mr = -100  
                
                if mu == -100 and md == -100 and ml == -100 and mr == -100:
                    break
            
        res = min(res, sum(row.count(0) for row in room_tmp))
        
        # print("----------")
        # for r in room_tmp:
        #     for v in r:
        #         print(v, end=" ")
        #     print()
        
        return
    
    model_num, x, y = coordinate_cctv[idx]
    for d_num, vector in enumerate(cctv_vector[model_num]):
        comb.append(d_num)
        cctv_check(comb, idx+1)
        comb.pop()
        
N, M = map(int, sys.stdin.readline().strip().split())
room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
coordinate_cctv = []
comb = []
cctv_vector = [
    None,
    [
        [-1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]
    ],
    [
        [0, 0, -1, 1],
        [-1, 1, 0, 0]
    ],
    [
        [-1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, -1, 0],
        [-1, 0, -1, 0]
    ], 
    [
        [-1, 0, -1, 1],
        [-1, 1, 0, 1],
        [0, 1, -1, 1],
        [-1, 1, -1, 0]
    ],
    [
        [-1, 1, -1, 1]
    ]
    ]
res = N * M

for y, row in enumerate(room):
    for x, v in enumerate(row):
        if v != 0 and v != 6:
            coordinate_cctv.append((v, x, y))

coordinate_cctv.sort( key=lambda x: x[0], reverse=True )

cctv_check([], 0)
    
print(res)