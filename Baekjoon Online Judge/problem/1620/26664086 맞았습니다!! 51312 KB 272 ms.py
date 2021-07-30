import sys

N, M = map(int, sys.stdin.readline().split())

dictByName = dict()
dictById = dict()

for n in range(1, N+1):
    pokemon = sys.stdin.readline().rstrip()
    dictByName[pokemon] = n
    dictById[n] = pokemon

for m in range(M):
    pokemon = sys.stdin.readline().rstrip()
    if pokemon.isdigit():
        print(dictById[int(pokemon)])
    else:
        print(dictByName[pokemon])