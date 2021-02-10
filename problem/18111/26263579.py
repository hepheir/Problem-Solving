import collections
import sys

INVENTORY = int(sys.stdin.readline().split()[2])
terrain = collections.Counter(map(int, sys.stdin.read().split()))

class ans:
    t = sys.maxsize
    z = 0

for target_z in range(255, -1, -1):
    to_rem = 0 # blocks to be removed
    to_pla = 0 # blocks to be placed
    for terrain_z, count in terrain.items():
        diff = terrain_z - target_z
        if diff > 0:
            to_rem += diff*count
        else:
            to_pla -= diff*count
    if to_pla > (to_rem+INVENTORY):
        continue
    etc = to_pla + to_rem*2
    if ans.t > etc or (ans.t == etc and ans.z < target_z):
        ans.t = etc
        ans.z = target_z

print(ans.t, ans.z)