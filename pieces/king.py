import absPiece
import gameBoard
from copy import copy
from pieces.nopiece import NoPiece


class King(absPiece.Piece):
    def __init__(self, xpos, ypos, color, name="king"):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name

    def validMove(self, board, x, y):
        if absPiece.outOfBounds(x, y):

            return False
        elif board.getPiece(x,y).getColor() == board.getPiece(self.xpos, self.ypos).getColor():

            return False
        elif abs(x - self.xpos) > 1 or abs(y - self.ypos) > 1:
            return False


        elif self.willKingInCheck(board, x, y):

            return False

        return True
