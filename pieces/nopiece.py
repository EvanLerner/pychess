


class NoPiece():
    def __init__(self, xpos, ypos, color="none", name="nopiece"):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name

    def validMove(self, board, x, y):
        False

    def getCords(self):
        return self.xpos, self.ypos

    def setCords(self, x, y):
        self.xpos = x
        self.ypos = y

    def getColor(self):
        return self.color

    def getName(self):
        return self.name
    def setFirstMoveFalse(self):
        pass
    def getValidMoves(self, board):
        pass