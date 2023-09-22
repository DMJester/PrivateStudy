#https://www.acmicpc.net/problem/1541

import sys

with open("./Greedy/1541/input.txt", 'r') as f:
    cal_str = f.readline().strip()
    
    tmp = ''
    num_list = []
    ops_list = []  
    
    res = 0
    res_list = [] 
    
    for c in cal_str:
        if c == '+' or c == '-':
            num_list.append(int(tmp))
            ops_list.append(c)
            tmp = ''
        else :
            tmp += c
    num_list.append(int(tmp))
    
    for idx, ops in enumerate(ops_list):
        if ops == '+':
            res_list.append( num_list[idx] + num_list[idx+1] )
        if ops == '-':
            res_list.append( num_list[idx] )
            num_list.append( num_list[idx+1] )
    
    for idx, r in enumerate(res_list):
        if idx == 0:
            res = r
        else :
            
            
    print(res)