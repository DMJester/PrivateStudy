import sys
from io import StringIO

sys.stdin = StringIO("".join(open("./BruteForce/1747/input.txt", "r").readlines()))\
    
def check_prime(number):
    if number == 1:
        return False
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            return False
    return True

def check_palindrom(number):
    tmp = list(map(int, str(number)))
    if tmp == tmp[::-1]:
        return True
    else:
        return False

N = int(sys.stdin.readline().strip())
    
now = N    
while 1:
   if check_prime(now):
       if check_palindrom(now):
           print(now)
           break
   now += 1 