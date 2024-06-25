import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/15823/input.txt", "r").readlines()))

N, M = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))
card_use = set()
res = 0

card_max_limit = len(cards) // M

left = 1
right = N
while left <= right:
    mid = (left + right) // 2
    
    start = 0
    end = 0
    card_cnt = 0
    pack_cnt = 0
    while start < N:
        if cards[end] not in card_use:
            card_use.add(cards[end])
            card_cnt += 1
            
            if end < N-1:
                end += 1    
                
            if card_cnt == mid:
                pack_cnt += 1
                card_cnt = 0
                start = end
                card_use.clear()
            
            if pack_cnt == M:
                break 
        else :
            if start < N:
                card_use.discard(cards[start])
            start += 1
            card_cnt -= 1
    
    if pack_cnt == M:
        res = mid
        left = mid + 1    
    else:
        right = mid - 1
        
print(res)
