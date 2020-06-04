import absPiece
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.nopiece import NoPiece
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook


class Board():
    def __init__(self):
        self.board = [[], [], [], [], [], [], [], []]
        self.board[0].append(Rook(0, 0, "black"))
        self.board[1].append(Knight(1, 0, "black"))
        self.board[2].append(Bishop(2, 0, "black"))
        self.board[3].append(Queen(3, 0, "black"))
        self.board[4].append(King(4, 0, "black"))
        self.board[5].append(Bishop(5, 0, "black"))
        self.board[6].append(Knight(6, 0, "black"))
        self.board[7].append(Rook(7, 0, "black"))
        for i in range(8):
            self.board[i].append(Pawn(i, 1, "black"))
        for i in range(4):
            for j in range(8):
                self.board[j].append(NoPiece(i + 2, j))
        for i in range(8):
            self.board[i].append(Pawn(i, 6, "white"))
        self.board[0].append(Rook(0, 7, "white"))
        self.board[1].append(Knight(1, 7, "white"))
        self.board[2].append(Bishop(2, 7, "white"))
        self.board[3].append(Queen(3, 7, "white"))
        self.board[4].append(King(4, 7, "white"))
        self.board[5].append(Bishop(5, 7, "white"))
        self.board[6].append(Knight(6, 7, "white"))
        self.board[7].append(Rook(7, 7, "white"))

    def getBoard(self):
        return self.board

    def getPiece(self, x, y):
        return self.board[x][y]

    def setPiece(self, piece, x, y):
        self.board[x][y] = piece
        piece.setCords(x, y)

    def movePiece(self, piece, x, y):
        piece.setFirstMoveFalse()
        self.setPiece(piece, x, y)

    def whiteKingInCheck(self):
        kingx = -1
        kingy = -1
        breakloop = False
        for i in range(8):
            if breakloop: break
            for j in range(8):
                if self.getPiece(i, j).getName() == "king" and self.getPiece(i, j).getColor() == "white":
                    kingx = i
                    kingy = j
                    breakloop = True

        for i in range(8):
            for j in range(8):
                if self.getPiece(i, j).getColor() == "black" and self.getPiece(i, j).validMove(self, kingx, kingy):
                    return True
        return False

    def blackKingInCheck(self):
        kingx = -1
        kingy = -1
        for i in range(8):
            for j in range(8):
                if self.getPiece(i, j).getName() == "king" and self.getPiece(i, j).getColor() == "black":
                    kingx = i
                    kingy = j

        for i in range(8):
            for j in range(8):
                if self.getPiece(i, j).getColor() == "white" and self.getPiece(i, j).validMove(self, kingx, kingy):
                    return True
        return False

    def whitewins(self):
        if self.blackKingInCheck():
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == "black":
                        for m in range(8):
                            for n in range(8):
                                if self.board[i][j].moveValid(m, n):
                                    return False
            return True
        return False

    def blackwins(self):
        if self.whiteKingInCheck():
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == "white":
                        for m in range(8):
                            for n in range(8):
                                if self.board[i][j].moveValid(m, n):
                                    return False
            return True
        return False

    def printBoard(self):
        for i in range(9):
            if i == 0:
                print("     ", end="")
            else:
                print(" ", i - 1, "  ", end="")
        print()
        for i in range(8):
            print(i, "  ", end="")
            for j in range(8):
                printBoardHelper(self.board[j][i].getName(), self.board[j][i].getColor(), i, j)
            print()


def printBoardHelper(piecename, color, i, j):
    if color == "white":
        switcher = {
            "rook": "  wR ",
            "bishop": "  wB ",
            "knight": "  wN ",
            "king": "  wK ",
            "queen": "  wQ ",
            "pawn": "  wP ",
        }
    elif color == "black":
        switcher = {
            "rook": "  bR ",
            "bishop": "  bB ",
            "knight": "  bN ",
            "king": "  bK ",
            "queen": "  bQ ",
            "pawn": "  bP ",
        }
    else:
        switcher = {
            "": ""
        }
    print(switcher.get(piecename, " " + str(j) + "," + str(i) + " "), end=" ")
