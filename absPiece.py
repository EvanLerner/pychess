from abc import ABC, abstractmethod
from copy import copy, deepcopy

import gameBoard
from pieces.nopiece import NoPiece


class Piece(ABC):

    def __init__(self, xpos, ypos, color, name, firstmove = True):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.name = name
        self.firstmove = firstmove

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
        self.firstmove = False

    def getValidMoves(self, board):
        print("start get valid moves")
        for i in range(8):
            for j in range(8):
                if board.getPiece(self.xpos, self.ypos).validMove(board, i, j):
                    print(i, " ", j)

    def pieceInWay(self, x, y, board):
        while x != self.xpos or y != self.ypos:
            if x == self.xpos:
                if y > self.ypos:
                    y = y - 1
                else:
                    y = y + 1
            elif y == self.ypos:
                if x > self.xpos:
                    x = x - 1
                else:
                    x = x + 1
            else:
                if x > self.xpos:
                    x = x - 1
                else:
                    x = x + 1
                if y > self.ypos:
                    y = y - 1
                else:
                    y = y + 1
            if(x == self.xpos and y == self.ypos):
                return False
            if board.getPiece(x, y).getName() != "nopiece":
                return True
        return False

    def willKingInCheck(self, board, x, y):
        board2 = deepcopy(board)
        copyPiece = copy(board.getPiece(self.xpos, self.ypos))
        board2.setPiece(copyPiece, x, y)
        board2.setPiece(NoPiece(self.xpos, self.ypos), self.xpos, self.ypos)

        if self.color == "white" and board2.whiteKingInCheck():
            return True
        elif self.color == "black" and board2.blackKingInCheck():
            return True
        return False

    @abstractmethod
    def validMove(self, board, x, y):
        pass


def outOfBounds(x, y):
    if x > 7 or x < 0 or y > 7 or y < 0:
        return True
    return False
