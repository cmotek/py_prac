from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        pointo = Point(p.getX() + 25, p.getY() + 25)
        pointt = Point(p.getX() - 25, p.getY() - 25)
        newshape = Rectangle(pointo, pointt)
        newshape.setOutline("red")
        newshape.setFill("red")
        newshape.draw(win)
    win.close()
main()
