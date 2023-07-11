import time as t
import os as o

class obj:
    def __init__(self, ylen, xlen, char):
        self.ylen = ylen
        self.xlen = xlen
        self.char = char
        self.string = ""
        for i in range(ylen):
            for i in range(xlen):
                self.string+=char
            self.string+="\n"

class grid:
    def __init__(self, ylen, xlen, char):
        self.ylen = ylen
        self.xlen = xlen
        self.char = char
        self.string = ""
        for i in range(ylen):
            for i in range(xlen):
                self.string+=char
            self.string+="\n"
    def __initgrid__(self, fps):
        interval = 1/fps
        while True:
            print(self.string)
            t.sleep(interval)
            o.system('cls')


grid1 = grid(20,20,".")
grid1.__initgrid__(44)
