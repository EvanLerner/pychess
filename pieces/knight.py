import absPiece
import gameBoard
from copy import copy

from pieces.nopiece import NoPiece


class Knight(absPiece.Piece):
    def __init__(self, xpos, ypos, color, name="knight"):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name

    def validMove(self, board, x, y):
        if absPiece.outOfBounds(x, y):
            #print("outtabounds")
            return False
        elif board.getPiece(x,y).getColor() == board.getPiece(self.xpos, self.ypos).getColor():
            #print("color")
            return False
        elif abs(y - self.ypos) * abs(x - self.xpos) != 2:
            #print("change in x * change in y != 2.... ")
            return False
        elif self.willKingInCheck(board, x, y):
            #print("king in check")
            return False
        return True
