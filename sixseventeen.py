from graphics import *


def main():


    win = GraphWin("shapemover")


    myshape = Circle(Point(100,100), 12)
    
    newCenter = Point(100,100)

    def MoveTo(shape, newCenter):
        for i in range(6):
            newCenter = win.getMouse()
            shape = Circle(newCenter, 12)
            shape.setOutline("black")
            shape.setFill("black")
            shape.draw(win)


    MoveTo(myshape, newCenter)












main()
