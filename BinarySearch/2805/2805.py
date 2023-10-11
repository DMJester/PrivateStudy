#https://www.acmicpc.net/problem/2805

import sys

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

N, M = map(int, sys.stdin.readline().strip().split())
wood_list = list(map(int, sys.stdin.readline().strip().split()))

wood_list.sort()

print(binary_search(0, max(wood_list)-1))