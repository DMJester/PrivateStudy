#https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3

import sys

def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: [x[1], x[0]])
    
    end_pos = 0
    print(targets)
    for t in targets:
        if t[0] >= end_pos:
            answer += 1
            end_pos = t[1]
    
    return answer

with open("./[Programers]/181188/input.txt", "r") as f:
    list = eval(f.readline())
    
    print(solution(list))