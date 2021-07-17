N = int(input())
S = input().split()

next_chr = None
playable = True

for palindrome in S:
    if next_chr is None:
        next_chr = palindrome[0]
    if next_chr != palindrome[0]:
        playable = False
        break

print(1 if playable else 0)