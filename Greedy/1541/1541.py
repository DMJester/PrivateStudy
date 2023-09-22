#https://www.acmicpc.net/problem/1541

import sys

cal_str = sys.stdin.readline().strip()
res = 0
    
p_list = cal_str.split('-')
m_list = []
sum = 0
for p in p_list:
    num_list = p.split('+')
    sum = 0
    for n in num_list:
        sum += int(n)
    m_list.append(sum)
        
for idx, m in enumerate(m_list):
    if idx == 0:
        res = m
    else :
        res -= m
    
print(res)