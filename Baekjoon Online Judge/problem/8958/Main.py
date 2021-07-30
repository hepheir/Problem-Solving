for testcase in range(int(input())):
    score = 0
    combo = 0
    for char in input():
        if char == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)
