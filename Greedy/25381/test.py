S = 'ABCBBACBABB'
print('Input:', S)
A, B, C = 0, 1, 2
alpha = [[] for _ in range(3)]
for idx, s in enumerate(S):
    alpha[eval(s)].append(idx)
print('A positions:', alpha[0])
print('B positions:', alpha[1])
print('C positions:', alpha[2])

# 현재 알고리즘 테스트
res = 0
now = C
while now >= 1:
    if len(alpha[now]) == 0:
        now -= 1
        if now == 0:
            break
    
    if len(alpha[now]) == 0:
        continue
        
    ec = alpha[now].pop()
    print(f'Looking for {chr(ord("A") + now - 1)} before position {ec}')
    
    for idx, sc in enumerate(reversed(alpha[now - 1])):
        if ec > sc:
            alpha[now - 1].pop(len(alpha[now - 1]) - 1 - idx)
            res += 1
            print(f'Found pair: {chr(ord("A") + now - 1)} at {sc}, {chr(ord("A") + now)} at {ec}')
            break
    
    print(f'Current result: {res}')
    print(f'Remaining A: {alpha[0]}, B: {alpha[1]}, C: {alpha[2]}')
    print()

print('Final result:', res)
