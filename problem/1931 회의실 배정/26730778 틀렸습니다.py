import collections
import sys
import typing

MAX_N = (1<<32)-1

class GreedySchedule:
    def __init__(self):
        self.start:int = None
        self.end:int = MAX_N
        self.count:int = 0
    
    def additem(self, end:int):
        if self.end == end:
            self.count += 1
        elif self.end > end:
            self.end = end
            self.count = 1


N = int(sys.stdin.readline())
SCHEDULE = collections.defaultdict(GreedySchedule)

for n in range(N):
    s, e = map(int, sys.stdin.readline().split())
    SCHEDULE[s].additem(e)

greedy_schedules:typing.List[GreedySchedule] = []
for start, schedule in SCHEDULE.items():
    schedule.start = start
    greedy_schedules.append(schedule)
greedy_schedules.sort(key=lambda x: (x.start, x.end))

def search(start):
    min_idx = None
    min_end = MAX_N
    for idx, schedule in enumerate(greedy_schedules):
        if schedule.start < start: continue
        if schedule.end >= min_end: break
        min_idx = idx
        min_end = min(schedule.end, min_end)
    return min_idx

answer = 0
curtime = 0
while (idx := search(curtime)) is not None:
    curtime = greedy_schedules.pop(idx).end
    answer += 1

print(answer)
