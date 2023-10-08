#https://www.acmicpc.net/problem/2110

import sys

def binary_search(start_idx, end_idx):
    while start_idx <= end_idx:
        mid = ( start_idx + end_idx ) // 2
        router_cnt = 0
        
    return

with open("./BinarySearch/2110/input.txt", "r") as f:
    N, C = map(int, f.readline().strip().split())
    house_list = []
    
    for _ in range(N):
        house_list.append(int(f.readline().strip()))
    
    house_list.sort()    

    binary_search(0, len(house_list)-1)
    
    