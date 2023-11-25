import sys

N = int(sys.stdin.readline().strip())
road_dist = list(map(int, sys.stdin.readline().strip().split()))
fuel_cost = list(map(int, sys.stdin.readline().strip().split()))
res = 0
now_cost = fuel_cost[0]

for idx, dist in enumerate(road_dist):
    if fuel_cost[idx] < now_cost:
        now_cost = fuel_cost[idx]
    res += now_cost * dist

print(res)