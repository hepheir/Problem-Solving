import sys

Y, X, INVENTORY = map(int, sys.stdin.readline().split())
TERRAIN = list(map(int, sys.stdin.read().split()))

existing_blocks = sum(TERRAIN)
area = X*Y

def calc_etc(z):
    # Calculates estimated time to complete
    blocks_need_to_be_placed = area*z - existing_blocks
    assert blocks_need_to_be_placed <= INVENTORY
    be_placed = 0
    be_removed = 0
    for blocks in TERRAIN:
        be_placed += max(z-blocks, 0)
        be_removed += max(blocks-z, 0)
    return be_placed*1 + be_removed*2

class Answer:
    etc = sys.maxsize
    z = 0

for z in range(256):
    try:
        etc = calc_etc(z)
        if (etc < Answer.etc) or (etc == Answer.etc and z > Answer.z):
            Answer.etc = etc
            Answer.z = z
    except:
        continue

print(Answer.etc, Answer.z)