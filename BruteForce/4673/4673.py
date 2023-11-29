#https://www.acmicpc.net/problem/4673
import sys

max = 10000
num_list = []
seq_list = []
self_number = []

for number in range(1, max+1):
    digit_list = list(map(int, str(number)))
    tmp_cal = number
    for n in digit_list:
        tmp_cal += n
    num_list.append(number)
    seq_list.append(tmp_cal)

self_number = sorted(list(set(num_list) - set(seq_list)))
for sn in self_number:
    print(sn)