#https://www.acmicpc.net/problem/1300
import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./Parametric Search/1300/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
res = 0

#1 ~ N*N 범위에서 B[k]가 x라고 가정
left = 1
right = N*N
while left <= right:
    x = (left + right) // 2
    front_sum = 0
    
    #1 ~ N 각 줄의 Index로 x를 나누고, N과 비교하여 작은 값을 front_sum에 누적
    #x보다 작은 숫자가 몇개인지 각 줄마다 세고 더하여 결과적으로 x라고 가정 했을때 누적합을 계산
    #이 때 x를 i로 나누기 때문에 x의 개수 까지 누적됨
    for i in range(1, N+1):
        front_sum += min(N, x//i)

    #B[k] 번째의 숫자를 구하려는 것이기 때문에 front_sum은 k와 같아야 할것이라 생각 했지만
    #위의 계산식 대로는 x의 개수 까지 누적합계에 더하기때문에 오차가 발생 하게됨
    #front_sum과 k를 비교하여 값이 k보다 크거나 같은 경우에 res를 갱신하고
    #while에서 빠져 나갈때 까지 left, right의 위치를 조절
    #front_sum의 의미는 각 x의 끝 경계를 의미하게 되고 k는 해당 범위안에 들어갔는지를 판단하게됨
    #N을 10, k를 11을 예제로 했을때의 답은 6이 나오게 되는데
    #[1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, ...]
    #해당 배열을 계산해보면 5일때 경계값은 10이고 6의 경계값은 14가 나오게됨
    #k는 11이기에 5의 경계값인 10은 넘어가고 6의 경계값인 14보다 작기에 11 ~ 14를 차지하는 6이 정답이게됨
    if front_sum >= k:
        res = x
        right = x - 1
    else:
        left = x + 1
        
print(res)