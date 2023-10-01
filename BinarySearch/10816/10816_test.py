#https://www.acmicpc.net/problem/10816

import sys

def binary_search_left(array, target, start_idx, end_idx):
    while start_idx <= end_idx:
        mid = int((start_idx + end_idx) / 2)
        
        if array[mid] >= target:
            end_idx = mid - 1
        else:
            start_idx = mid + 1
    return start_idx

def binary_search_right(array, target, start_idx, end_idx):
    while start_idx <= end_idx:
        mid = int((start_idx + end_idx) / 2)
        
        if array[mid] <= target:
            start_idx = mid + 1
        else:
            end_idx = mid - 1
    return end_idx

with open("./Sort/10816/input.txt", "r") as f:
    N = int(f.readline().strip())
    N_list = list(map(int, f.readline().strip().split()))
    M = int(f.readline().strip())
    M_list = list(map(int, f.readline().strip().split()))
    res = 0
    
    N_list.sort()
    
    for target in M_list:
        left = binary_search_left(N_list, target, 0, N-1)
        right = binary_search_right(N_list, target, 0, N-1)
        res = right - left + 1
        print(res)  
