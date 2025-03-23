#https://www.acmicpc.net/problem/3109
#빵집(가스도둑김원웅)

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BFS&DFS/3109/input.txt", "r").readlines()))

def dfs(start, depth, sp): 
  global res

  if depth == C-1:
    res += 1
    end_check[sp] = True
    return True
  
  for dir in dirs:
    if start + dir[0] >= 0 and start + dir[0] < R and depth + dir[1] >= 0 and depth + dir[1] < C and pipe_map[start+dir[0]][depth+dir[1]] != 'x':
      if end_check[sp] == False:
        pipe_map[start+dir[0]][depth+dir[1]] = 'x'
        dfs(start + dir[0], depth + 1, sp)
  return

R, C = map(int, sys.stdin.readline().strip().split())
pipe_map = [[c for c in sys.stdin.readline().strip()] for _ in range(R)]
dirs = [(-1, 1), (0, 1), (1,1)]
end_check = [False for _ in range(R)]
res = 0

for start in range(R):
  pipe_map[start][0] = 'x'
  dfs(start, 0, start)

print(res)