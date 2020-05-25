from abc import ABC, abstractmethod


class Piece(ABC):

    def __init__(self, xpos, ypos, color, name):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name

    def getCords(self):
        return self.xpos, self.ypos

    def setCords(self, x, y):
        self.xpos = x
        self.ypos = y

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    @abstractmetod
    def validMove(self, x, y):
        pass