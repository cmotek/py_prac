from graphics import *

def main():
    win = GraphWin()
    aCircle = Circle(Point(100,100), 10)
    bCircle = Circle(Point(100,100), 20)
    cCircle = Circle(Point(100,100), 30)
    dCircle = Circle(Point(100,100), 40)
    eCircle = Circle(Point(100,100), 50)
    eCircle.setOutline("black")
    dCircle.setFill("black")
    cCircle.setFill("blue")
    bCircle.setFill("red")
    aCircle.setFill("yellow")
    eCircle.draw(win)
    dCircle.draw(win)
    cCircle.draw(win)
    bCircle.draw(win)
    aCircle.draw(win)
    
main()
