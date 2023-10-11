#https://www.acmicpc.net/problem/2805

import sys
"""
def binary_search( H, start_idx, end_idx ):
    mid = 0
    while start_idx <= end_idx:
        mid = int( ( start_idx + end_idx ) / 2 )
        if wood_list[mid] == H:
            break
        elif wood_list[mid] > H:
            end_idx = mid - 1
        elif wood_list[mid] < H:
            start_idx = mid + 1
    return mid

with open("./Sort/2805/input.txt", "r") as f:
    N, M = map(int, f.readline().strip().split())
    wood_list = list(map(int, f.readline().strip().split()))
    res = 0
    
    wood_list.sort()
    
    for H in range(wood_list[-1]-1, 0, -1):
        sum = 0
        for i in range(binary_search(H, 0, len(wood_list)-1), len(wood_list)):
            if wood_list[i] > H:
                sum += wood_list[i] - H
        if sum == M:
            res = H
            break;
    print(H)
"""

def binary_search( start_idx, end_idx ):
    res = 0
    while start_idx <= end_idx:
        log = 0
        mid = ( start_idx + end_idx ) // 2
        for wood in wood_list:
            if wood > mid:
                log += wood - mid
        
        if log < M:
            end_idx = mid - 1
        else:
            res = mid
            start_idx = mid + 1
    return res

with open("./BinarySearch/2805/input.txt", "r") as f:
    N, M = map(int, f.readline().strip().split())
    wood_list = list(map(int, f.readline().strip().split()))
    
    wood_list.sort()
    
    print(binary_search(0, max(wood_list)-1))