#사이트 제출 시 79%에서 [틀렸습니다] 상태.
#샘플 자동 생성을 통해 정답 코드(란돔)와 비교하며 틀린 샘플을 찾아봤을때 나오지 않음
#백준에 질문 글 올려놓고 대기 중 https://www.acmicpc.net/board/view/146209

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./TwoPoint/16472/input.txt", "r").readlines()))

N = int(sys.stdin.readline().strip())
cat_lang = list(sys.stdin.readline())
res = 0

start = 0
end = 0

char_cnt = 0
char_use = dict() 

while start <= end and end < len(cat_lang):
    char_use_cnt = len(char_use)
    if char_use_cnt < N:
        if cat_lang[end] not in char_use:
            char_use[cat_lang[end]] = 0
        char_use[cat_lang[end]] += 1
        char_cnt += 1
        res = max(res, char_cnt)
        end += 1
    elif char_use_cnt == N and (cat_lang[end] in char_use):
        char_use[cat_lang[end]] += 1
        char_cnt += 1
        res = max(res, char_cnt)
        end += 1
    else:
        if cat_lang[start] in char_use:
            char_use[cat_lang[start]] -= 1
            if char_use[cat_lang[start]] <= 0:
                char_use.pop(cat_lang[start])
        char_cnt -= 1
        start += 1

print(res)