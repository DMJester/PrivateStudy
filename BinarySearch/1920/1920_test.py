#https://www.acmicpc.net/problem/1920

import sys

def binary_search(array, target, start_idx, end_idx):
    while start_idx <= end_idx:
        mid = int((start_idx + end_idx) / 2)
        
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end_idx = mid - 1
        else:
            start_idx = mid + 1
    return 0

with open("./BinarySearch/1920/input.txt", "r") as f:
    N = int(f.readline().strip())
    N_list = list(map(int, f.readline().strip().split()))
    M = int(f.readline().strip())
    M_list = list(map(int, f.readline().strip().split()))
    res = 0
    
    N_list.sort()

    for idx in range(M):
        target = M_list[idx]
        
        res = binary_search(N_list, target, 0, N-1)    
        print(res)