#https://www.acmicpc.net/problem/1446
import sys
from io import StringIO
import heapq

sys.stdin = StringIO("".join(open("./DynamicProgramming/1446/input.txt", "r").readlines()))

N, D = map(int, sys.stdin.readline().strip().split())
shortcuts = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ] 
running_in_the_90s = [float('inf') for _ in range(10001)]

q = heapq()
q = 

    
print(graph)