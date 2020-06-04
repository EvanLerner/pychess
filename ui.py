from turtle import *

from absPiece import Piece
from images import *

nameswitcher ={
"knight": "n",
"bishop": "b",
"king" : "k",
"queen": "q",
"pawn" : "p",
"rook" : "r"
}
colorswitcher ={
"white": "w",
"black": "b"
}

def makeWindow(board):
    import turtle

    screen = turtle.Screen()

    # this assures that the size of the screen will always be 400x400 ...
    screen.setup(530, 530)

    # ... which is the same size as our image
    # now set the background to our space image
    screen.bgpic("chessboard.png")

    # Or, set the shape of a turtle
    #screen.addshape("rocketship.png")
    #turtle.shape("rocketship.png")

    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.speed("fastest")
    
    turtles = []
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

    for i in range(8):
        for j in range(8):
            reali = i-4
            realj = j-4
            newturtle = Turtle(visible = False)
            newturtle.penup()
            newturtle.setx(reali*66 + 30)
            newturtle.sety(realj*66 + 30)

            if board.getPiece(i,j).getName() != "nopiece":
                newturtle.shape(piece2picture(board.getPiece(i, j)))
                newturtle.showturtle()
            #get the turtle name file
            turtles.append(newturtle)

    screen.listen()
    turtle.update()
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
