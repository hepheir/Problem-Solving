import sys

MAX_N = (1<<32)-1

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self) -> str: return f'({self.start}, {self.end})'
    def __repr__(self) -> str: return self.__str__()

class MeetingList:
    list = []
    
    @classmethod
    def register(cls, start, end):
        cls.list.append(Meeting(start, end))
    
    @classmethod
    def sort(cls):
        cls.list.sort(key=lambda m: (m.start, m.end))

    @classmethod
    def get_maximum_possible_meetings(cls):
        cls.list.sort(reverse=True, key=lambda m:(m.start, m.end))
        answer = 0
        fastest_end = 0
        while cls.list:
            meeting = cls.list.pop()
            if meeting.end < fastest_end:
                fastest_end = meeting.end
            if meeting.start >= fastest_end:
                fastest_end = meeting.end
                answer += 1
        return answer
    

N = int(sys.stdin.readline())

for n in range(N):
    MeetingList.register(*map(int, sys.stdin.readline().split()))

print(MeetingList.get_maximum_possible_meetings())