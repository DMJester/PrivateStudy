import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./23032/input.txt", "r").readlines()))

N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().strip().split()))
res = 0

prev = 10000 * 2000
for mid in range(1, N):
    left = mid - 1
    right = mid
    left_sum = 0
    right_sum = 0

    left_sum += W[left]
    right_sum += W[right]
    while True:
        diff = abs(left_sum - right_sum)   
        if diff < prev:
            prev = diff
            res = (left_sum+right_sum)
        elif diff == prev:
            prev = diff
            res = max(res, (left_sum+right_sum))
        
        if left_sum < right_sum and left > 0:
            left -= 1
            left_sum += W[left]
        elif left_sum > right_sum and right < N-1:
            right += 1
            right_sum += W[right]
        elif left_sum == right_sum:
            if left > 0:
                left -= 1
                left_sum += W[left]
            if right < N-1:
                right += 1
                right_sum += W[right]
        else:
            break

print(res)