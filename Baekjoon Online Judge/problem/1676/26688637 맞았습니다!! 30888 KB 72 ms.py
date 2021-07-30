import math
import sys

N = int(sys.stdin.readline())
if N:
    facto = list(str(math.factorial(N)))
    answer = 0
    while facto.pop() == '0':
        answer += 1
else:
    answer = 0
print(answer)