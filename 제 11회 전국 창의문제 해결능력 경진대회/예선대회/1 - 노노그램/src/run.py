from Table import Table
from Interval import *



def pause():
    import cv2
    cv2.waitKey(0)


def init():
    global width, height
    global colIntervalLists, rowIntervalLists
    with open('1 - 노노그램/data/sample_input.txt', 'r') as f:
        width, height = map(int, f.readline().split())
        inputs = [list(map(int, line.split())) for line in f.readlines()]
    colIntervalLists = list(map(ColIntervalList, inputs[:width]))
    rowIntervalLists = list(map(RowIntervalList, inputs[width:]))

class List:
    def __init__(self, iter):
        self.list = iter

class FilledList(List):
    pass

class EmptyList(List):
    pass


def create_line(line, intervalList):
    ls = []
    ls.append(EmptyList())
    for _ in range(len(intervalList)):
        ls.append(FilledList())
        ls.append(EmptyList())
    return ls


def initial_routine(table):
    pass

def main_routine(table):
    for x in range(width):
        intervalList = colIntervalLists[x]
        if intervalList.minimum_length
        for interval in colIntervalLists[x]:
            pass



if __name__ == '__main__':
    init()
    table = Table(width, height)
    table.set(2,2)
    table.print()

    pause()