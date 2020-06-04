from pip._vendor.distlib.compat import raw_input

import ui

from gameBoard import Board
from pieces.king import King
from pieces.nopiece import NoPiece
from pieces.queen import Queen
from pieces.rook import Rook

validcords = []
for i in range (8):
    for j in range(8):
        validcords.append(str(i) + ", " + str(j))

def turn(whiteTurn, board):
    validMoves = []
    input = raw_input("What piece do you want to move? enter coords like '3, 5': ")
    if input not in validcords:
        print("not a vlaid cord")
        return whiteTurn
    xcord = int(input[0])
    ycord = int(input[3])
    if board.getPiece(xcord, ycord).getColor() != "white" and whiteTurn:
        print("piece isnt white and its whites trun")
        return whiteTurn
    if board.getPiece(xcord, ycord).getColor() != "black" and not whiteTurn:
        print("piece isnt black and its blacks trun")
        return whiteTurn
    for i in range(8):
        for j in range(8):
            if (board.getPiece(xcord, ycord).validMove(board, i, j)):
                validMoves.append(str(i) + ", " + str(j))
    if len(validMoves) == 0:
        print("There are no valid moves for that piece")
        return whiteTurn

    print("The valid moves are: ")
    for i in validMoves:
        print(i)
    print("valid moves: ", validMoves)
    inputmove = raw_input("Type what move you want: ")
    if inputmove not in validMoves:
        print("not a validmove")
        return whiteTurn
    xmove = int(inputmove[0])
    ymove = int(inputmove[3])
    if inputmove in validMoves:
        board.movePiece(board.getPiece(xcord, ycord), xmove, ymove)
        board.setPiece(NoPiece(xcord,ycord),xcord,ycord)
        return not whiteTurn


def main():

    ui.makeWindow(Board())



if __name__ == "__main__":
    main()
