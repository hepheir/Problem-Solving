import sys
input = sys.stdin.readline

def solve(n_of_intervals:int, max_duration:int, interval_starts:list, interval_ends:list):
    n_robots = 0
    remaining_time = max_duration
    current_time_unit = 0
    # Order intervals in ascent order
    tmp_dict = dict()
    for start, end in zip(interval_starts, interval_ends):
        tmp_dict[start] = (start, end)
    ordered_intervals = [tmp_dict[idx] for idx in sorted(tmp_dict)]
    # Calc min num of required robots
    for start, end in ordered_intervals:
        if current_time_unit < start:
            current_time_unit = start
        while end - current_time_unit > 0:
            n_robots += 1
            current_time_unit += max_duration
    return n_robots

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        S, E = [], []
        for n in range(N):
            si, ei = map(int, input().split())
            S.append(si)
            E.append(ei)
        ans = solve(N, K, S, E)
        print('Case #{0}: {1}'.format(t+1, ans))