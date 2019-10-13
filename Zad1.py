from graphics import *

def CreateWindow():
    ##Window
    win = GraphWin("MyPaint", 750, 600)
    win.setBackground(color_rgb(96,240,128))

    ##x, y labels and text
    x1label = Text(Point(30, 20), "x1: ")
    x2label = Text(Point(200, 20), "x2: ")
    y1label = Text(Point(30, 70), "y1: ")
    y2label = Text(Point(200, 70), "y2: ")
    x1label.draw(win)
    x2label.draw(win)
    y1label.draw(win)
    y2label.draw(win)

    x1 = Entry(Point(100,20),10)
    x2 = Entry(Point(270, 20), 10)
    y1 = Entry(Point(100, 70), 10)
    y2 = Entry(Point(270, 70), 10)
    x1.draw(win)
    x2.draw(win)
    y1.draw(win)
    y2.draw(win)

    ##Buttons
    lineButton = Rectangle(Point(400, 20), Point(500, 70))
    rectangleButton = Rectangle(Point(550, 20), Point(650, 70))
    ovalButton = Rectangle(Point(470, 90), Point(570, 140))
    quitButton = Rectangle(Point(160, 116), Point(220, 146))

    lineButton.setFill("white")
    rectangleButton.setFill("white")
    ovalButton.setFill("white")

    quitText = Text(Point(190, 133), "Exit")
    lineText = Text(Point(450, 45), "Line")
    rectangleText = Text(Point(600, 45), "Rectangle")
    ovalText = Text(Point(520, 115), "Oval")


    lineButton.draw(win)
    rectangleButton.draw(win)
    ovalButton.draw(win)
    quitButton.draw(win)
    quitText.draw(win)
    lineText.draw(win)
    rectangleText.draw(win)
    ovalText.draw(win)


    win.getMouse()
    win.close()

CreateWindow()

