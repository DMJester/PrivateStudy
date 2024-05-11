import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./test_240504/1543/input.txt").readlines()))

document = sys.stdin.readline().strip()
keyword = sys.stdin.readline().strip()
document_size = len(document)
keyword_size = len(keyword)
res = 0

search_idx = 0
while search_idx < document_size:
    if document[search_idx] == keyword[0]:
        for k_idx, k in enumerate(keyword):
            if search_idx + k_idx <= document_size-1:
                if document[search_idx + k_idx] != k:
                    search_idx += 1
                    break
            else:
                search_idx += 1
                break
            if k_idx == keyword_size-1:
                res += 1
                search_idx += keyword_size
    else:
        search_idx += 1

print(res)