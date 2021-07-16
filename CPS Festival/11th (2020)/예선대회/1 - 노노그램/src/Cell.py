class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class UnknownCell(Cell):
    pass

class EmptyCell(Cell):
    pass

class FilledCell(cell):
    def __init__(self, x, y, colIntervalId=None, rowIntervalId=None):
        return super(FilledCell, self).__init__(x, y)
        self.colIntervalId = colIntervalId
        self.rowIntervalId = rowIntervalId