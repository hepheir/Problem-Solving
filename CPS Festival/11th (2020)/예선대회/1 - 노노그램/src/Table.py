from Cell import *

class Table:
    def __init__(self, width, height):
        self.table = None
        self.width = width
        self.height = height
        self.padding = True

        self.new_table(width, height)


    def new_table(self, width, height, padding=None):
        if padding is not None:
            self.padding = padding
        if self.padding:
            width += 2
            height += 2
        table = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(UnknownCell())
            table.append(row)
        self.table = table


    def set(self, x, y):
        self.table[y][x] = FILL
    

    def clear(self, x, y):
        self.table[y][x] = EMPTY


    def print(self, scaler=16):
        import cv2
        import numpy as np
        frame = cv2.resize(
            np.array(self.table, dtype=np.uint8),
            (self.width * scaler, self.height * scaler),
            fx=0,
            fy=0,
            interpolation=cv2.INTER_NEAREST)
        cv2.imshow('ANSWER', frame)


    def read(self):
        TRANSLATE = {
            '1' : FILL,
            '0' : EMPTY,
            '?' : UNKNOWN}
        with open('1 - 노노그램/data/sample_output.txt', 'r') as f:
            lines = f.readlines()
        for x in range(self.width):
            for y in range(self.height):
                self.table[y][x] = TRANSLATE[lines[y][x]]


    def save(self):
        TRANSLATE = {
            FILL : '1',
            EMPTY : '0',
            UNKNOWN : '?'}
        with open('1 - 노노그램/data/sample_output.txt', 'w') as f:
            for y in range(height):
                for x in range(width):
                    f.write(TRANSLATE[self.table[y][x]])
                f.write('\n')


