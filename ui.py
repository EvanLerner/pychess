import turtle
from turtle import *

from absPiece import Piece
from gameBoard import Board
from images import *

turtles = [[], [], [], [], [], [], [], []]
screen = turtle.Screen()

frank = Turtle(visible=False)

frankspieces = []

gameboard = Board()
mainpiece = []
nameswitcher = {
    "knight": "n",
    "bishop": "b",
    "king": "k",
    "queen": "q",
    "pawn": "p",
    "rook": "r"
}
colorswitcher = {
    "white": "w",
    "black": "b"
}
numswitcher = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7
}


def makeWindow():
    # this assures that the size of the screen will always be 400x400 ...
    screen.setup(530, 530)
    stage1 = True
    screen.bgpic("chessboard.png")
    turtle.penup()
    # tracer makes it move faster
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.speed("fastest")

    screen.addshape("images/bb.gif")
    screen.addshape("images/bk.gif")
    screen.addshape("images/bn.gif")
    screen.addshape("images/bp.gif")
    screen.addshape("images/bq.gif")
    screen.addshape("images/br.gif")
    screen.addshape("images/wb.gif")
    screen.addshape("images/wn.gif")
    screen.addshape("images/wp.gif")
    screen.addshape("images/wq.gif")
    screen.addshape("images/wr.gif")
    screen.addshape("images/wk.gif")

    turtles = createBoard(gameboard)

    turtle.onscreenclick(getBoardPiece)
    screen.listen()
    turtle.mainloop()


def piece2picture(piece):
    color = piece.getColor()
    name = piece.getName()
    picturename = ""
    if color == "none":
        return ""
    picturename += "images/"
    picturename += colorswitcher[color]
    picturename += nameswitcher[name]
    picturename += ".gif"
    return picturename


def createBoard(board):
    for i in range(8):
        for j in range(8):
            reali = i - 4
            realj = j - 4
            newturtle = Turtle(visible=False)
            newturtle.penup()
            newturtle.setx(reali * 66 + 30)
            newturtle.sety(realj * 66 + 30)

            if board.getPiece(i, j).getName() != "nopiece":
                newturtle.shape(piece2picture(board.getPiece(i, j)))
                newturtle.showturtle()
            # get the turtle name file
            turtles[i].append(newturtle)
    turtle.update()
    return turtles

def getXposYpos(x,y):
    addonx = 3
    addony = 3
    if x >= 0:
        addonx += 1
    if y >= 0:
        addony += 1
    xpos, ypos = (int(x / 66.25) + addonx, int(y / 66.25) + addony)
    return xpos,ypos

def setBoardPiece(x, y):
    xpos, ypos = getXposYpos(x,y)
    if gameboard.getPiece(xpos, ypos) in frankspieces:
        frankspieces.clear()
        frank.clear()
        mainpiecex, mainpiecey = mainpiece[0].getCords()
        gameboard.movePiece(mainpiece[0], xpos, ypos)
        turtles[xpos][ypos].goto((xpos-4) * 66+30 , (ypos-4)*66 +30)
        turtles[xpos][ypos].showturtle()
        turtles[xpos][ypos].shape(piece2picture(gameboard.getPiece(xpos, ypos)))
        turtles[xpos][ypos].showturtle()
        turtles[mainpiecex][mainpiecey].ht()

        turtle.onscreenclick(getBoardPiece)
        turtle.update()

        print("it is in franks pieces")
    else:
        print("not in franks pieces")
        frankspieces.clear()
        frank.clear()
        turtle.onscreenclick(getBoardPiece)
        turtle.update()

def getBoardPiece(x, y):
    frank.clear()
    frank.penup()
    frank.color("red")
    frank.fillcolor("red")
    addonx = 3
    addony = 3
    if x >= 0:
        addonx += 1
    if y >= 0:
        addony += 1

    xpos, ypos = (int(x / 66.25) + addonx, int(y / 66.25) + addony)

    mainpiece.clear()
    mainpiece.append(gameboard.getPiece(xpos, ypos))
    if mainpiece[0].getName() == "nopiece":
        turtle.onscreenclick(getBoardPiece)
    else:
        for i in range(8):
            for j in range(8):
                if mainpiece[0].validMove(gameboard, i, j):
                    reali = i - 4
                    realj = j - 4
                    frank.setx(reali * 66 + 32)
                    frank.sety(realj * 66 + 25)
                    frank.pendown()
                    frank.begin_fill()
                    frank.circle(10)
                    frank.end_fill()
                    frank.penup()
                    frankspieces.append(gameboard.getPiece(i, j))
        turtle.update()
        turtle.onscreenclick(setBoardPiece)


def convert(num):
    return numswitcher[num]
