import absPiece
import gameBoard
from copy import copy
from pieces.nopiece import NoPiece


class Pawn(absPiece.Piece):
    def __init__(self, xpos, ypos, color, name="pawn", firstmove=True):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name
        self.firstmove = firstmove

    def validMove(self, board, x, y):
        if absPiece.outOfBounds(x, y):
            return False
        elif board.getPiece(x, y).getColor() == self.color:
            return False
        elif self.pieceInWay(x,y,board):
            return False
        elif board.getPiece(x,y).getColor() == oppositeColor(self.color) and x-self.xpos == 0:
            return False
        elif x == self.xpos and y == self.ypos:
            return False
        elif abs(self.ypos - y) > 2:
            return False
        elif abs(self.ypos - y) > 1 and self.xpos - x != 0:
            return False
        elif self.ypos == y:
            return False
        elif abs(self.xpos - x) > 1:
            return False
        elif abs(self.xpos - x) * (self.ypos - y) == 1:
            if board.getPiece(x,y).getColor() == "none" or board.getPiece(x,y).getColor() == self.color:
                return False


        if self.color == "white":
            if self.ypos - y < 0:
                # print("white piece going down")
                return False

        if self.color == "black":
            if self.ypos - y > 0:
                # print("black piece going up")
                return False

        if not (self.firstmove):
            if abs(y - self.ypos) != 1:
                # print("first move more then one")
                return False

        elif self.willKingInCheck(board, x, y):
            # print("will king in check")
            return False

        return True
def oppositeColor(string):
    if string == "white":
        return "black"
    elif string == "black":
        return "white"
    return "none"