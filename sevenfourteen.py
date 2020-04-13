from graphics import *
import math

def main():
    win = GraphWin()
    Text(Point(40,20), "    Radius:").draw(win)
    Text(Point(40,50), "    Y-Intercept:").draw(win)
    radius_input = Entry(Point(100,20), 5)
    ycept_input = Entry(Point(100,50), 5)
    radius_input.setText("0")
    ycept_input.setText("0")
    radius_input.draw(win)
    ycept_input.draw(win)

    win.getMouse()

    try:
        radius = int(radius_input.getText())
        ycept = int(ycept_input.getText())

        mycircle = Circle(Point(100,100), radius)
        mycircle.draw(win)
        ycoord = 100 - ycept
        myline = Line(Point(50,ycoord), Point(150,ycoord))
        myline.draw(win)
        x1 = math.sqrt(radius * radius - ycept * ycept)
        x2 = -(math.sqrt(radius * radius - ycept * ycept))
        truex1 = 100 + x1
        truex2 = 100 + x2
        win.plot(truex1, ycoord, "red")
        win.plot(truex2, ycoord, "red")
        print(truex1)
        print(truex2)

    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("That line does not cross the circle")
   





main()
