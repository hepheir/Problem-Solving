class Interval:
    def __init__(self, length=0):
        self.length = length
        self.start = None
        self.end = None

    @property
    def done(self):
        if self.length == 0:
            return True
        elif (self.start is None) or (self.end is None):
            return False
        else:
            return (self.end - self.start + 1) == self.length


class IntervalList:
    def __init__(self, numbers):
        self.list = []
        self.read(numbers)
    
    @property
    def done(self):
        for interval in self.list:
            if not interval.done:
                return False
        return True

    
    def read(self, numbers):
        for length in numbers:
            self.list.append(Interval(length))

    @property
    def required_length(self):
        lengthList = [interval.length for interval in self.list]
        l = sum(lengthList)
        l += len(self.list)-1 # 칠해진 칸들 사이 빈칸 고려
        return l

    @property
    def check(self, line):
        rl = self.required_length
        

class RowIntervalList(IntervalList):
    pass


class ColIntervalList(IntervalList):
    pass