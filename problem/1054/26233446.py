import itertools
import sys

N = int(sys.stdin.readline())
words = list(map(lambda x: x.rstrip(), sys.stdin.readlines()))
answer = 0

def isPallindrome(sentence):
    for i in range(len(sentence)//2):
        if sentence[i] != sentence[-1-i]:
            return False
    return True

for n in range(1, len(words)+1):
    for perm in itertools.permutations(words, n):
        if isPallindrome(''.join(perm)):
            answer += 1

print(answer)