import absPiece
import gameBoard
from copy import copy
from pieces.nopiece import NoPiece


class Bishop(absPiece.Piece):
    def __init__(self, xpos, ypos, color, name="bishop"):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name


    def validMove(self, board, x, y):
        if absPiece.outOfBounds(x, y):
            # print("first false")
            return False
        elif board.getPiece(x, y).getColor() == board.getPiece(self.xpos, self.ypos).getColor():
            # print("second false")
            return False
        elif self.pieceInWay(x, y, board):
            # print("third false")
            return False
        elif x == self.xpos and y == self.ypos:
            # print("fourth false")
            return False
        elif abs(x - self.xpos) != abs(y - self.ypos):
            # print("fifth false")
            return False
        elif self.willKingInCheck(board, x, y):
            return False

        return True
