from graphics import *


##Window
win = GraphWin("MyPaint", 1200, 600)
win.setBackground(color_rgb(96,240,128))

x1 = Entry(Point(100, 20), 10)
x2 = Entry(Point(270, 20), 10)
y1 = Entry(Point(100, 70), 10)
y2 = Entry(Point(270, 70), 10)


##Buttons
lineButton = Rectangle(Point(400, 20), Point(500, 70))
rectangleButton = Rectangle(Point(550, 20), Point(650, 70))
ovalButton = Rectangle(Point(470, 90), Point(570, 140))
quitButton = Rectangle(Point(160, 116), Point(220, 146))


drawingarea = Rectangle(Point(30,200), Point(700, 570))


##x, y labels and text
x1label = Text(Point(30, 20), "x1: ")
x2label = Text(Point(200, 20), "x2: ")
y1label = Text(Point(30, 70), "y1: ")
y2label = Text(Point(200, 70), "y2: ")

## Texts for buttons
quitText = Text(Point(190, 133), "Exit")
rectangleText = Text(Point(600, 45), "Rectangle")
ovalText = Text(Point(520, 115), "Oval")
lineText = Text(Point(450, 45), "Line")

## RGB, CMYK
Rlabel = Text(Point(800,200), "R:")
Glabel = Text(Point(800, 300), "G:")
Blabel = Text(Point(800, 400), "B:")

RInput = Entry(Point(870,200),10)
GInput = Entry(Point(870,300),10)
BInput = Entry(Point(870,400),10)

Clabel = Text(Point(1000, 150), "C:")
Mlabel = Text(Point(1000, 250), "M:")
Ylabel = Text(Point(1000, 350), "Y:")
Klabel = Text(Point(1000, 450), "K:")

CInput = Entry(Point(1070, 150), 10)
MInput = Entry(Point(1070, 250), 10)
YInput = Entry(Point(1070, 350), 10)
KInput = Entry(Point(1070, 450), 10)

colorArea = Rectangle(Point(900, 500), Point(1000, 550))

rgb_scale = 255
cmyk_scale = 100


def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, cmyk_scale

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / float(rgb_scale)
    m = 1 - g / float(rgb_scale)
    y = 1 - b / float(rgb_scale)

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy)
    m = (m - min_cmy)
    y = (y - min_cmy)
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    CInput.setText(c * cmyk_scale)
    MInput.setText(m * cmyk_scale)
    YInput.setText(y * cmyk_scale)
    KInput.setText(k * cmyk_scale)
 ##   return c*cmyk_scale, m*cmyk_scale, y*cmyk_scale, k*cmyk_scale

def cmyk_to_rgb(c, m, y, k, cmyk_scale, rgb_scale=255):
    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))

    r_round = round(r)
    g_round = round(g)
    b_round = round(b)

    RInput.setText(r_round)
    GInput.setText(g_round)
    BInput.setText(b_round)



    ##return r, g, b



def CreateWindow():

    x1label.draw(win)
    x2label.draw(win)
    y1label.draw(win)
    y2label.draw(win)

    x1.draw(win)
    x2.draw(win)
    y1.draw(win)
    y2.draw(win)

    lineButton.setFill("white")
    rectangleButton.setFill("white")
    ovalButton.setFill("white")


    lineButton.draw(win)
    rectangleButton.draw(win)
    ovalButton.draw(win)
    quitButton.draw(win)
    quitText.draw(win)
    lineText.draw(win)
    rectangleText.draw(win)
    ovalText.draw(win)

    ## Drawings - label and area
    drawingLabel = Text(Point(70, 180), "Drawing area:")
    drawingLabel.draw(win)
    drawingarea.setFill("white")
    drawingarea.draw(win)

    #RGB, CMYK
    Rlabel.draw(win)
    Glabel.draw(win)
    Blabel.draw(win)

    RInput.draw(win)
    GInput.draw(win)
    BInput.draw(win)

    Clabel.draw(win)
    Mlabel.draw(win)
    Ylabel.draw(win)
    Klabel.draw(win)

    CInput.draw(win)
    MInput.draw(win)
    YInput.draw(win)
    KInput.draw(win)

    colorArea.draw(win)

def DrawLine():
    drawedline = Line(Point(x1.getText(), y1.getText()), Point(x2.getText(), y2.getText()))
    drawedline.draw(win)
    drawedline.setFill(color_rgb((int)(RInput.getText()),(int)(GInput.getText()),(int)(BInput.getText())))

def DrawRect():
    drawedrectangle = Rectangle(Point(x1.getText(), y1.getText()), Point(x2.getText(), y2.getText()))
    drawedrectangle.draw(win)
    drawedrectangle.setOutline(color_rgb((int)(RInput.getText()), (int)(GInput.getText()), (int)(BInput.getText())))

def DrawOval():
    drawedoval = Oval(Point(x1.getText(), y1.getText()), Point(x2.getText(), y2.getText()))
    drawedoval.draw(win)
    drawedoval.setOutline(color_rgb((int)(RInput.getText()), (int)(GInput.getText()), (int)(BInput.getText())))

def Colors():
    colorArea.setFill(color_rgb((int) (RInput.getText()),(int) (GInput.getText()) ,(int) (BInput.getText())))

def main():
    CreateWindow()


    while True:

        clicked=win.getMouse()

        if (int)(x1.getText()) < (drawingarea.getP1()).getX() or (int)(x1.getText()) > (drawingarea.getP2()).getX() or (int)(x2.getText()) < (drawingarea.getP1()).getX() or (int)(x2.getText()) > (drawingarea.getP2()).getX() or (int)(y1.getText()) < (drawingarea.getP1()).getY() or (int)(y1.getText()) > (drawingarea.getP2()).getY() or (int)(y2.getText()) < (drawingarea.getP1()).getY() or (int)(y2.getText()) > (drawingarea.getP2()).getY():
            mes = GraphWin("False parameters", 300, 150)
            mesText = Text(Point(120, 50), "Please select parameters:\n for x - between 30 and 700\n and for y - between 200 and 570.")
            mesText.draw(mes)
            okButton = Rectangle(Point(120,100), Point(180, 120))
            okButton.draw(mes)
            okText = Text(Point(150, 110), "OK")
            okText.draw(mes)
            mes.getMouse()
            mes.close()

        elif clicked.getX() > (lineButton.getP1()).getX() and clicked.getX() < (lineButton.getP2()).getX() and clicked.getY() > (lineButton.getP1()).getY() and clicked.getY() < (lineButton.getP2()).getY():
            DrawLine()

        elif clicked.getX() > (rectangleButton.getP1()).getX() and clicked.getX() < (rectangleButton.getP2()).getX() and clicked.getY() > (rectangleButton.getP1()).getY() and clicked.getY() < (rectangleButton.getP2()).getY():
            DrawRect()

        elif clicked.getX() > (ovalButton.getP1()).getX() and clicked.getX() < (ovalButton.getP2()).getX() and clicked.getY() > (ovalButton.getP1()).getY() and clicked.getY() < (ovalButton.getP2()).getY():
            DrawOval()

        elif clicked.getX() > (quitButton.getP1()).getX() and clicked.getX() < (quitButton.getP2()).getX() and clicked.getY() > (quitButton.getP1()).getY() and clicked.getY() < (quitButton.getP2()).getY():
           win.close()

        if RInput.getText()=="":
            cmyk_to_rgb((float)(CInput.getText()), (float)(MInput.getText()), (float)(YInput.getText()),
                        (float)(KInput.getText()), 100, 255)
        else:
            rgb_to_cmyk((float)(RInput.getText()), (float)(GInput.getText()), (float)(BInput.getText()))
            Colors()





main()


##win.getMouse()
