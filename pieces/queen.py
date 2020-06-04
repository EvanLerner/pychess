import absPiece
import gameBoard
from copy import copy
from pieces.nopiece import NoPiece


class Queen(absPiece.Piece):
    def __init__(self, xpos, ypos, color, name="queen"):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name

    def validMove(self, board, x, y):
        if absPiece.outOfBounds(x, y):
            return False
        elif board.getPiece(x,y).getColor() == board.getPiece(self.xpos, self.ypos).getColor():
            return False
        elif x == self.xpos and y == self.ypos:
            return False
        elif self.pieceInWay(x,y,board):
            return False
        elif not (x == self.xpos or y == self.ypos) and abs(x - self.xpos) != abs(y - self.ypos):
            return False
        elif self.willKingInCheck(board, x, y):
            return False

        return True