#https://www.acmicpc.net/problem/10775
#공항

import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./10775/input.txt", "r").readlines()))

G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())
planes = [int(sys.stdin.readline().strip()) for _ in range(P)]
res = 0

in_gates = sorted(set(planes))
gates = [[0,0]]
gates += [[0, 0] for _ in range(G)]

prev = 0
for gate in in_gates:
	gates[gate][0] = gate - prev
	prev = gate

deadlock = False

for idx, d_gate in enumerate(planes):
	if deadlock == True:
		break

	if gates[d_gate][0] - gates[d_gate][1] >= 1:
		gates[d_gate][1] += 1
		res += 1
	else:
		prev_gate = d_gate
		while prev_gate > 0:
			prev_gate -= gates[prev_gate][0]
			if gates[prev_gate][0] - gates[prev_gate][1] >= 1:
				gates[prev_gate][1] += 1
				res += 1
				break
		if prev_gate <= 0:
			deadlock = True

print(res)