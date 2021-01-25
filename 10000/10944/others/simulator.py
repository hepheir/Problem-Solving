from random import randint

def solve():
    # return randint(1, 10000)
    return '1'

total_matches = 0
total_tries = 0
memory = 0

while True:
    total_tries += 1
    if str(randint(1,10000)) == str(solve()):
        total_matches += 1
        memory = total_tries
        print(f'정답률: {total_matches/total_tries*100:.6f}%  [{total_tries}번 중]       ', end='\r')