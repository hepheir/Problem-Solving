import math
import sys

N = int(sys.stdin.readline())
answer = 0
for c in str(math.factorial(N)):
    if c == '0':
        answer += 1
print(answer)