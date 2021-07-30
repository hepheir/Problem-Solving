import sys
import typing

class Meeting:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end

class MeetingList:
    list:typing.List[Meeting] = []
    
    @classmethod
    def register(cls, start, end):
        cls.list.append(Meeting(start, end))
    
    @classmethod
    def sort(cls):
        cls.list.sort(reverse=True, key=lambda m:(m.start, m.end))

    @classmethod
    def get_maximum_possible_meetings(cls) -> int:
        cls.sort()
        answer = 0
        fastest_end = 0
        while cls.list:
            meeting = cls.list.pop()
            if meeting.end < fastest_end:
                fastest_end = meeting.end
            elif meeting.start >= fastest_end:
                fastest_end = meeting.end
                answer += 1
        return answer
    

N = int(sys.stdin.readline())

for n in range(N):
    MeetingList.register(*map(int, sys.stdin.readline().split()))

print(MeetingList.get_maximum_possible_meetings())