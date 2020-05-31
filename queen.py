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


        board2 = copy(board)
        board2.setPiece(Queen(x, y, self.color), x, y)
        board2.setPiece(NoPiece(self.xpos, self.ypos), self.xpos, self.ypos)

        if self.color == "white" and board2.whiteKingInCheck:
            return False
        elif self.color == "black" and board2.blackKingInCheck:
            return False

        if abs(y-self.ypos) - abs(x-self.xpos) == 0:
            return True
        if x == self.xpos or y == self.ypos:
            return True
        return True