import collections
import sys

INVENTORY = int(sys.stdin.readline().split()[2])
terrain = collections.Counter(map(int, sys.stdin.read().split()))

class ans:
    etc = sys.maxsize
    z = 0

for target_z in range(257):
    rm = 0 # blocks to be removed
    pl = 0 # blocks to be placed
    for terrain_z, count in terrain.items():
        diff = terrain_z - target_z
        if diff > 0:
            rm += diff*count
        else:
            pl -= diff*count
    if pl > (rm + INVENTORY):
        continue
    etc = pl + rm*2
    if etc <= ans.etc:
        ans.etc = etc
        ans.z = target_z

print(ans.etc, ans.z)