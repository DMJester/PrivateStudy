#https://school.programmers.co.kr/learn/courses/30/lessons/60063
import sys
from io import StringIO
from collections import deque

sys.stdin = StringIO("".join(open("./[Programers]/60063/input.txt", "r").readlines()))
board = [list(map(int, sys.stdin.readline().strip().split())) for y in range(5)]

def rotate_drone(cx, cy, sub):
    if sub == 'U':
        return
    elif sub == 'D':
        return
    elif sub == 'L':
        return
    elif sub == 'R':
        return
    
#상하좌우 이동 좌표 계산
def move_drone(x, y, direction):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    mx = x + dx[direction]
    my = y + dy[direction]
        
    return mx, my

def bfs():    
    q = deque()
    q.append((0, 0))
    
    while q:
        cx, cy = q.pop()
        
        for direction in range(4):
            mx, my = move_drone(cx, cy, direction)
            if mx >= 0 and mx <= board_size and my >= 0 and my <= board_size:
                if board[my][mx] == 0:
                    board[my][mx] = 2
                    q.append((mx, my))

def solution(board):
    answer = 0
    
    global board_size
    board_size = len(board) - 1
    
    bfs()
    
    for n in board:
        print(n)
        
    return answer

solution(board)