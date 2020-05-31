from gameBoard import Board
from pieces.bishop import Bishop
from pieces.king import King
from pieces.pawn import Pawn
from pieces.rook import Rook


def main():
    board = Board()


    board.printBoard()

    #print(board.getPiece(4,4).validMove(board,7,3))



if __name__ == "__main__":
    main()
