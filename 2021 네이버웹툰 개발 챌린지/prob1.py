from collections import defaultdict


def solution(lottery):
    is_winner = defaultdict(lambda: False)
    counter = defaultdict(lambda: 0)
    n_winners = 0
    n_tries = 0

    for user_id, is_jackpot in lottery:
        if is_jackpot and not is_winner[user_id]:
            counter[user_id] += 1
            is_winner[user_id] = True
            n_winners += 1
            n_tries += counter[user_id]
        elif not is_jackpot and not is_winner[user_id]:
            counter[user_id] += 1

    if n_winners == 0:
        return 0
    else:
        return n_tries // n_winners
